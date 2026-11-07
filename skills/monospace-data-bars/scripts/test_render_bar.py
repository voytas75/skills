import unittest

from render_bar import InputError, render


class RenderBarTests(unittest.TestCase):
    def test_default_block_template(self):
        result = render({"unit": "%", "items": [{"label": "CPU", "value": 82}]})
        self.assertEqual(result, "CPU  ██████████░░  82%")

    def test_ascii_variant(self):
        result = render({"variant": "ascii", "unit": "%", "items": [{"label": "CPU", "value": 50}]})
        self.assertEqual(result, "CPU  ######......  50%")

    def test_zero_and_maximum(self):
        result = render({"unit": "%", "items": [{"label": "zero", "value": 0}, {"label": "full", "value": 100}]})
        self.assertIn("zero  ░░░░░░░░░░░░  0", result)
        self.assertIn("full  ████████████  100", result)

    def test_status_requires_explicit_status(self):
        with self.assertRaises(InputError):
            render({"variant": "status", "items": [{"label": "CPU", "value": 80}]})

    def test_status_uses_supplied_label(self):
        result = render({"variant": "status", "unit": "%", "items": [{"label": "CPU", "value": 80, "status": "WARN"}]})
        self.assertTrue(result.endswith("80%  WARN"))

    def test_delta_requires_previous(self):
        with self.assertRaises(InputError):
            render({"variant": "delta", "items": [{"label": "CPU", "value": 80}]})

    def test_percentage_delta_is_percentage_points(self):
        result = render({"variant": "delta", "unit": "%", "items": [{"label": "CPU", "value": 82, "previous": 70, "period": "last week"}]})
        self.assertTrue(result.endswith("+12 pp vs last week"))

    def test_threshold_marker(self):
        result = render({"variant": "threshold", "unit": "%", "threshold": 70, "items": [{"label": "CPU", "value": 82}]})
        self.assertIn("│ = threshold", result)
        self.assertIn("target 70%", result)

    def test_out_of_range_rejected(self):
        with self.assertRaises(InputError):
            render({"unit": "%", "items": [{"label": "CPU", "value": 101}]})

    def test_invalid_scale_rejected(self):
        with self.assertRaises(InputError):
            render({"unit": "%", "min": 10, "max": 10, "items": [{"label": "x", "value": 10}]})

    def test_boolean_is_not_numeric(self):
        with self.assertRaises(InputError):
            render({"unit": "%", "items": [{"label": "x", "value": True}]})

    def test_auto_resolves_to_default(self):
        result = render({"variant": "auto", "unit": "%", "items": [{"label": "x", "value": 100}]})
        self.assertIn("████████████", result)


if __name__ == "__main__":
    unittest.main()
