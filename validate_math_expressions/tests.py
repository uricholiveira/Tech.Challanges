import pytest

from main import check_expression, EXPRESSION_ACCEPTED, EXPRESSION_NOT_ACCEPTED


class TestMethod:
    @pytest.mark.parametrize(argnames="expression, expected", argvalues=[
        ('(x + y)', EXPRESSION_ACCEPTED),
        ('(x + y) * z', EXPRESSION_ACCEPTED),
        ('x - z + (y)', EXPRESSION_ACCEPTED),
        ('(x * y) + (x * z)', EXPRESSION_ACCEPTED),
        ('x ) y', EXPRESSION_NOT_ACCEPTED),
        ('(x)(y)', EXPRESSION_NOT_ACCEPTED),
        ('x + y + z', EXPRESSION_ACCEPTED),
        ('(x) + (y) + (z * x)', EXPRESSION_ACCEPTED),
        ('x + )', EXPRESSION_ACCEPTED),
        ('(x) + (', EXPRESSION_ACCEPTED),
        ('x + (* y)', EXPRESSION_ACCEPTED),
    ])
    def test(self, expression, expected):
        result = check_expression(expression)

        assert result in expected
