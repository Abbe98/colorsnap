# Colorsnap

Python package for snaping/rounding colors to other colors/palettes.

Colorsnap comes with predefined palettes for CSS 2-4 and can also take custom ones defined by you as input and then snap/round a specified color to the closes one in the given palette.

## Installing

```python
pip install colorsnap
```

# Usage Examples

```python
import colorsnap

'''
Available palettes:
 - CSS_2
 - CSS_2_1
 - CSS_3
 - CSS_4
'''

colorsnap.snap_color(colorsnap.palettes.CSS_3, '#0000ba')
# >>> ('#0000ba', 'mediumblue')

# Using a custom palette
palette = {
    'black': '#000000',
    'gray': '#808080',
    'white': '#ffffff',
}

colorsnap.snap_color(palette, '#0000ba')

# Using a custom palette with unnamed colors
palette = ['#4286f4', '#414449']

color_snap.snap_color(palette, '#5588db')
# >>> ('#5588db', '#4286f4')

```
