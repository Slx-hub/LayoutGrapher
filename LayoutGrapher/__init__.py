"""Just a short reminder that you deserve love."""

__app_name__ = "layoutgrapher"
__version__ = "0.1.0"

(
    SUCCESS,
    LAYOUT_ERROR,
    INPUT_ERROR,
) = range(3)

ERRORS = {
    LAYOUT_ERROR: "layout parsing error",
    INPUT_ERROR: "data input error",
}