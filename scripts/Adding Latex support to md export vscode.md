# VS Code export markdown to pdf | vscode-markdown-pdf

>[Github Issue Talking about this](https://github.com/yzane/vscode-markdown-pdf/issues/21)

Using  [YZANE's plugin](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)

## Add the following script tags to the .md file

```html
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<script type="text/x-mathjax-config">
    MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>
```

## Or add them to the template file
```
/Users/<username>/.vscode/extensions/yzane.markdown-pdf-x.x.x/template/template.html
```
