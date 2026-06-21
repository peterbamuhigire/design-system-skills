#!/usr/bin/env python3
"""
Color Palette Generator
Generates color palettes from brand colors using color theory principles.
"""

import re
import colorsys
import json
from typing import Tuple, List, Dict


class ColorPalette:
    """Generate harmonious color palettes from a brand color."""

    def __init__(self, hex_color: str):
        """Initialize with a brand color in hex format."""
        self.hex_color = hex_color.lstrip('#')
        self.rgb = self._hex_to_rgb(self.hex_color)
        self.hsl = self._rgb_to_hsl(self.rgb)

    @staticmethod
    def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        """Convert hex to RGB."""
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def _rgb_to_hsl(rgb: Tuple[int, int, int]) -> Tuple[int, int, int]:
        """Convert RGB (0-255) to HSL (0-360, 0-100, 0-100)."""
        r, g, b = [x / 255.0 for x in rgb]
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return int(h * 360), int(s * 100), int(l * 100)

    @staticmethod
    def _hsl_to_rgb(h: int, s: int, l: int) -> Tuple[int, int, int]:
        """Convert HSL (0-360, 0-100, 0-100) to RGB (0-255)."""
        h, s, l = h / 360.0, s / 100.0, l / 100.0
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return tuple(int(x * 255) for x in (r, g, b))

    @staticmethod
    def _rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
        """Convert RGB to hex."""
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

    def _hsl_to_hex(self, h: int, s: int, l: int) -> str:
        """Convert HSL to hex."""
        rgb = self._hsl_to_rgb(h, s, l)
        return self._rgb_to_hex(rgb)

    def monochromatic(self, num_colors: int = 4) -> List[str]:
        """Generate monochromatic palette (variations of one hue)."""
        h, s, _ = self.hsl
        lightnesses = [25, 45, 65, 85][:num_colors]
        return [self._hsl_to_hex(h, s, l) for l in lightnesses]

    def complementary(self) -> Tuple[str, str]:
        """Generate complementary palette (180° apart)."""
        h, s, l = self.hsl
        complement_h = (h + 180) % 360
        return self._hsl_to_hex(h, s, l), self._hsl_to_hex(complement_h, s, l)

    def analogous(self, spread: int = 30) -> List[str]:
        """Generate analogous palette (adjacent colors)."""
        h, s, l = self.hsl
        hues = [
            (h - spread) % 360,
            h,
            (h + spread) % 360
        ]
        return [self._hsl_to_hex(hue, s, l) for hue in hues]

    def split_complementary(self) -> List[str]:
        """Generate split-complementary palette."""
        h, s, l = self.hsl
        complement_h = (h + 180) % 360
        colors = [
            self._hsl_to_hex(h, s, l),                    # Primary
            self._hsl_to_hex((complement_h - 30) % 360, s, l),  # First split
            self._hsl_to_hex((complement_h + 30) % 360, s, l),  # Second split
        ]
        return colors

    def triadic(self) -> List[str]:
        """Generate triadic palette (120° apart)."""
        h, s, l = self.hsl
        hues = [h, (h + 120) % 360, (h + 240) % 360]
        return [self._hsl_to_hex(hue, s, l) for hue in hues]

    def tetradic(self) -> List[str]:
        """Generate tetradic palette (90° apart)."""
        h, s, l = self.hsl
        hues = [h, (h + 90) % 360, (h + 180) % 360, (h + 270) % 360]
        return [self._hsl_to_hex(hue, s, l) for hue in hues]

    def get_tints_and_shades(self, num_steps: int = 9) -> List[str]:
        """Generate tints and shades (lightness variations)."""
        h, s, _ = self.hsl
        lightnesses = [int(100 * i / (num_steps - 1)) for i in range(num_steps)]
        return [self._hsl_to_hex(h, s, l) for l in lightnesses]

    def semantic_palette(self) -> Dict[str, str]:
        """Generate complete semantic palette with feedback colors."""
        h, s, l = self.hsl

        # Primary color and variations
        primary = self._hsl_to_hex(h, s, l)
        primary_dark = self._hsl_to_hex(h, s, max(0, l - 20))
        primary_light = self._hsl_to_hex(h, s, min(100, l + 20))

        # Complementary for secondary
        secondary_h = (h + 180) % 360
        secondary = self._hsl_to_hex(secondary_h, s, l)

        return {
            "primary": primary,
            "primary_dark": primary_dark,
            "primary_light": primary_light,
            "secondary": secondary,
            "success": "#10B981",      # Green
            "warning": "#F59E0B",      # Amber
            "error": "#EF4444",        # Red
            "info": "#3B82F6",         # Blue
            "text_primary": "#1F2937",    # Dark gray
            "text_secondary": "#6B7280",  # Medium gray
            "border": "#E5E7EB",          # Light gray
            "background": "#FFFFFF"       # White
        }

    def generate_report(self) -> Dict:
        """Generate comprehensive color report."""
        return {
            "input_color": f"#{self.hex_color}",
            "hsl": f"hsl({self.hsl[0]}, {self.hsl[1]}%, {self.hsl[2]}%)",
            "rgb": f"rgb({self.rgb[0]}, {self.rgb[1]}, {self.rgb[2]})",
            "palettes": {
                "monochromatic": self.monochromatic(),
                "analogous": self.analogous(),
                "complementary": list(self.complementary()),
                "split_complementary": self.split_complementary(),
                "triadic": self.triadic(),
                "tetradic": self.tetradic(),
                "tints_and_shades": self.get_tints_and_shades(),
            },
            "semantic": self.semantic_palette()
        }


def generate_palette_from_hex(hex_color: str, scheme: str = "semantic") -> Dict:
    """Generate color palette from hex color."""
    palette = ColorPalette(hex_color)

    schemes = {
        "monochromatic": palette.monochromatic,
        "analogous": palette.analogous,
        "complementary": palette.complementary,
        "split_complementary": palette.split_complementary,
        "triadic": palette.triadic,
        "tetradic": palette.tetradic,
        "tints_and_shades": palette.get_tints_and_shades,
        "semantic": palette.semantic_palette,
        "report": palette.generate_report,
    }

    if scheme not in schemes:
        return {"error": f"Unknown scheme: {scheme}. Available: {list(schemes.keys())}"}

    result = schemes[scheme]()
    return result if isinstance(result, dict) else {"colors": result}


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python palette_generator.py <hex_color> [scheme]")
        print("Schemes: monochromatic, analogous, complementary, split_complementary, triadic, tetradic, tints_and_shades, semantic, report")
        sys.exit(1)

    hex_color = sys.argv[1]
    scheme = sys.argv[2] if len(sys.argv) > 2 else "semantic"

    result = generate_palette_from_hex(hex_color, scheme)
    print(json.dumps(result, indent=2))
