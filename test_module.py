import unittest
import time_series_visualizer


class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_title(self):
        self.assertEqual(
            self.ax.get_title(),
            "Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
        )

    def test_line_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Date")
        self.assertEqual(self.ax.get_ylabel(), "Page Views")


class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_legend(self):
        legend = self.ax.get_legend()
        self.assertIsNotNone(legend)
        self.assertEqual(legend.get_title().get_text(), "Months")


class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()
        self.axes = self.fig.axes

    def test_box_plot_count(self):
        self.assertEqual(len(self.axes), 2)

    def test_box_plot_titles(self):
        self.assertEqual(self.axes[0].get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(
            self.axes[1].get_title(), "Month-wise Box Plot (Seasonality)"
        )


if __name__ == "__main__":
    unittest.main()
