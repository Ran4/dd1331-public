### Git log-alias
`git log` är ett användbart kommando. Utformatet kan modifieras på många olika sätt, här är ett exempel på
ett alias som kan vara användbart:
```bash
alias gl='git log -n 10 --graph --pretty=format:"%Cred%h%Creset%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit --date=relative'
```

Exempel (utan färger):
```
* b256da0 (HEAD -> master) Add ovningar folder and ovning_01.md (3 minutes ago) <Rasmus Ansin>
* 4ede5cb (origin/master, origin/HEAD) Initial commit (5 minutes ago) <Rasmus Ansin>
```
