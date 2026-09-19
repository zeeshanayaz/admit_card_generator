import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from admit_card_generator import generate_pdf
from config import EXAM_NAME, ISSUE_DATE, SCHOOL_ADDRESS, SCHOOL_NAME, SCHOOL_SUBTITLE


class AdmitCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AMFS Admit Card Generator")
        self.root.geometry("620x530")
        self.root.resizable(False, False)

        self.excel_path = None
        self.settings = {
            "school_name": tk.StringVar(value=SCHOOL_NAME),
            "school_subtitle": tk.StringVar(value=SCHOOL_SUBTITLE),
            "school_address": tk.StringVar(value=SCHOOL_ADDRESS),
            "exam_name": tk.StringVar(value=EXAM_NAME),
            "issue_date": tk.StringVar(value=ISSUE_DATE),
        }

        title = tk.Label(
            root,
            text="AMFS Examination Admit Card Generator",
            font=("Arial", 18, "bold"),
        )
        title.pack(pady=(28, 8))

        subtitle = tk.Label(
            root,
            text="Mid-Term Examination 2026-27 | 2 Admit Cards per A4",
            font=("Arial", 10),
        )
        subtitle.pack(pady=(0, 25))

        settings_frame = tk.LabelFrame(
            root, text="Admit Card Details", padx=12, pady=8
        )
        settings_frame.pack(fill="x", padx=34, pady=(0, 12))

        fields = [
            ("School Name", "school_name"),
            ("School Subtitle", "school_subtitle"),
            ("School Address", "school_address"),
            ("Exam Name", "exam_name"),
            ("Issue Date", "issue_date"),
        ]
        for row, (label, key) in enumerate(fields):
            tk.Label(settings_frame, text=label, anchor="w", width=18).grid(
                row=row, column=0, sticky="w", padx=(0, 8), pady=3
            )
            tk.Entry(settings_frame, textvariable=self.settings[key], width=58).grid(
                row=row, column=1, sticky="ew", pady=3
            )
        settings_frame.columnconfigure(1, weight=1)

        self.file_label = tk.Label(
            root,
            text="No Excel file selected",
            fg="gray",
            wraplength=520,
        )
        self.file_label.pack(pady=5)

        tk.Button(
            root,
            text="Select Student Excel File",
            width=28,
            height=2,
            command=self.select_excel,
        ).pack(pady=8)

        tk.Button(
            root,
            text="Generate Admit Cards PDF",
            width=28,
            height=2,
            command=self.generate,
        ).pack(pady=8)

        tk.Button(
            root,
            text="Exit",
            width=12,
            command=root.destroy,
        ).pack(pady=8)

    def select_excel(self):
        path = filedialog.askopenfilename(
            title="Select Student Excel File",
            filetypes=[
                ("Excel files", "*.xlsx *.xlsm"),
                ("All files", "*.*"),
            ],
        )
        if path:
            self.excel_path = Path(path)
            self.file_label.config(
                text=f"Selected: {self.excel_path.name}",
                fg="black",
            )

    def generate(self):
        if not self.excel_path:
            messagebox.showwarning(
                "Excel Required",
                "Please select the student Excel file first.",
            )
            return

        try:
            output_path = self.excel_path.parent / "AMFS_Admit_Cards.pdf"
            pdf = generate_pdf(
                self.excel_path,
                output_path,
                **{
                    key: variable.get().strip()
                    for key, variable in self.settings.items()
                },
            )

            messagebox.showinfo(
                "Success",
                f"Admit cards generated successfully.\n\n{pdf}",
            )
        except Exception as exc:
            messagebox.showerror(
                "Generation Error",
                str(exc),
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = AdmitCardApp(root)
    root.mainloop()
