from trafaret.lang import CSharp


def test_csharp_comment() -> None:
    lang = CSharp()
    comment = '// this is a comment \n'
    m = lang.comment.match(comment)
    assert m
    assert m.group(0) == comment
