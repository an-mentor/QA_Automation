class ValidationHelper:
    @staticmethod
    def check_required_validations(page, form_fields):
        """Check HTML5 validation messages for each required input."""
        for field in form_fields:
            try:
                message = page.eval_on_selector(
                    field, "el => el.validationMessage"
                )
                if message:
                    print(f"[validation] {field}: {message}")
            except Exception as e:
                print(f"[validation] Could not get message for {field}: {e}")
