"""we making the filters for compstagram."""

__author__ = "730644820"
__template__ = "https://24ss2.comp110.com/static/compstagram/"

from .support import (
    Color,
    Bitmap,
    Request,
    Base64ImageStr,
    bitmap_to_base64,
    FilterSettings,
)


def main(request: Request) -> Base64ImageStr:
    """Primary endpoint for to the Compstagram backend.
    This function is called each time a new image is loaded, a filter is
    added/removed, or a filter's amount is changed."""
    image: Bitmap = request.image

    if filter in request.filters:
        image = filter.process(image)
    return bitmap_to_base64(image)


def get_filter_types() -> list[FilterSettings]:
    """Produces a list of default Filters users can choose from.
    As you add new Filter classes, add additional instances of FilterSettings
    to this list for them to appear in the front-end. The name must match the Filter's
    class name and the amount represents the default intensity of a filter
    when added to the front-end."""
    return [
        FilterSettings(name="InvertFilter", amount=1.0),
        FilterSettings(name="BorderFilter", amount=0.05),
        FilterSettings(name="BrightnessFilter", amount=0.5),
        FilterSettings(name="SaturationFilter", amount=0.0),
    ]


class InvertFilter:
    """The InvertFilter's process method is provided to you as an example for
    some ideas on how to implement an image processing algorithm given an input
    image. All of yours will also iterate through each pixel using a nested for loop,
    and modify each pixel by applying logic and/or arithmetic to manipulate it.
    """

    amount: float

    def __init__(self, amount: float):
        self.amount = amount

    def process(self, bitmap: Bitmap) -> Bitmap:
        for rows in range(bitmap.height):
            for cols in range(bitmap.width):
                pixel = bitmap.pixels[rows][cols]
                red_inverted = 255 - pixel.red
                green_inverted = 255 - pixel.green
                blue_inverted = 255 - pixel.blue

                red_delta = int((red_inverted - pixel.red) * self.amount)
                green_delta = int((green_inverted - pixel.green) * self.amount)
                blue_delta = int((blue_inverted - pixel.blue) * self.amount)

                pixel.red += red_delta
                pixel.green += green_delta
                pixel.blue += blue_delta
        return bitmap


class BorderFilter:
    """Produce a border around the Bitmap."""

    amount: float
    color: Color

    def __init__(self, amount: float):
        """Initializes the Border filter with a thickness amount and a default color."""
        self.amount = amount
        self.color = Color(75, 156, 211)

    def process(self, bitmap: Bitmap) -> Bitmap:
        border_thickness: int = (bitmap.width / 2) * self.amount
        for rows in range(bitmap.height):
            for cols in range(bitmap.width):
                pixel = bitmap.pixels[rows][cols]
                if (
                    cols < border_thickness
                    or cols >= bitmap.width - border_thickness
                    or rows < border_thickness
                    or rows >= bitmap.height - border_thickness
                ):
                    pixel.red = 75
                    pixel.green = 156
                    pixel.blue = 211
        return bitmap


class BrightnessFilter:
    amount: float

    def __init__(self, amount: float):
        self.amount = amount

    def process(self, bitmap: Bitmap) -> Bitmap:
        factor_brightness: float = (self.amount - 0.5) * 2.0
        for rows in range(bitmap.height):
            for cols in range(bitmap.width):
                pixel = bitmap.pixels[rows][cols]

                red_delta = int(factor_brightness * pixel.red)
                green_delta = int(factor_brightness * pixel.green)
                blue_delta = int(factor_brightness * pixel.blue)

                pixel.red += red_delta
                pixel.green += green_delta
                pixel.blue += blue_delta

        return bitmap


class SaturationFilter:
    amount: float

    def __init__(self, amount: float):
        self.amount = amount

    def process(self, bitmap: Bitmap) -> Bitmap:
        factor_saturation: float = (0.5 - self.amount) * 2.0
        for rows in range(bitmap.height):
            for cols in range(bitmap.width):
                pixel = bitmap.pixels[rows][cols]

                component_average: float = (pixel.red + pixel.green + pixel.blue) / 3.0
                red_delta = int((component_average - pixel.red) * factor_saturation)
                green_delta = int((component_average - pixel.green) * factor_saturation)
                blue_delta = int((component_average - pixel.blue) * factor_saturation)

                pixel.red += red_delta
                pixel.green += green_delta
                pixel.blue += blue_delta

        return bitmap
