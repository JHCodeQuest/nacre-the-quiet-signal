# Nacre — The Quiet Signal

A Python desktop space exploration game about Captain Joe and his maintenance drone, Patch. Learn programming and engineering ideas through practical story decisions, rather than syntax quizzes.

Early learning prototype: the current build shows Kestrel Station and two clickable dialogue/investigation actions. The full chapter, save system and RPG features are planned, not implemented.

## Run locally

Requires Python 3.11 or later. Python 3.13 with pygame 2.6.1 has been reported working during development. In PyCharm, select a project virtual environment, then run:

```powershell
python -m pip install -r requirements.txt
python main.py
```

Click **Inspect the signal** and **Ask Patch about the ship** to display their responses. Close the window to exit.

## Development direction

- **Phase 1:** a complete linear narrative chapter with exploration, evidence, concepts, communications, saves and desktop packaging. Contextual interactions support one fixed story progression.
- **Phase 2:** RPG elements: branching missions, ship upgrades, resources, crew relationships and persistent consequences.

See [the task roadmap](docs/roadmap.md) and [public project board](https://github.com/users/JHCodeQuest/projects/12). Steam is a possible future distribution target; no Steam integration or release is currently available.

## Licence

Original project code is MIT licensed; see [LICENSE](LICENSE). pygame and any future third-party assets retain their own licences. Include applicable dependency notices when distributing packaged builds.
