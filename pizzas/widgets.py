from django.forms import widgets


class Select2Widget(widgets.SelectMultiple):
    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css",
            )
        }
        js = (
            "//ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js",
            "select2-start.js",
        )

    def __init__(self, attrs={}, choices=(), *args, **kwargs):
        options = kwargs.pop("select2_options", {})
        new_attrs = self.update_attrs(options, attrs)
        super().__init__(new_attrs)
        self.choices = list(choices)

    def update_attrs(self, options, attrs):
        attrs = self.add_class(attrs)
        multiple = options.pop("multiple", False)
        if multiple:
            attrs["multiple"] = "true"
        return attrs

    def add_class(self, attrs):
        class_name = attrs.pop("class", "")
        if class_name:
            attrs["class"] = "{} {}".format(class_name, "select2-widget")
        else:
            attrs["class"] = "select2-widget"

        return attrs


    def format_value(self, value):
        value = value.split("|") if value else ""
        return super().format_value(value)

    def value_from_datadict(self, data, files, name: str):
        return "|".join(data.getlist("ingredientes"))

    