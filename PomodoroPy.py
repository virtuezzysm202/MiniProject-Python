import time
from rich.console import Console
from rich.progress import Progress

console = Console()

def countdown(minutes, label):
    seconds = minutes * 60
    with Progress() as progress:
        task = progress.add_task(f"[cyan]{label}", total=seconds)
        while seconds > 0:
            minutes_left = seconds // 60
            seconds_left = seconds % 60
            time_str = f"{minutes_left:02d}:{seconds_left:02d}"
            progress.update(task, advance=1, description=f"[green]{label}: [bold]{time_str}")
            time.sleep(1)
            seconds -= 1
    console.print(f"[bold green]{label} finished!")


if __name__ == "__main__":
    countdown(1, "Pomodoro") #can edit minute in here, example 25 minute
