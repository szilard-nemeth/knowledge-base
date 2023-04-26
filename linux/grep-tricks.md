### Parse from alias
```
alias goto-dex-7712-clitesting | grep -o "=.*" | cut -d "'" -f2 | cut -d ' ' -f2
```