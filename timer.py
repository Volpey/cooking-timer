import time
import asyncio


class TimerManager:
    def __init__(self, page, timer_text, timer_status, start_button, stop_button):
        self.page = page
        self.timer_text = timer_text
        self.timer_status = timer_status
        self.start_button = start_button
        self.stop_button = stop_button
        self.running = False

    def start(self, recipe):
        if recipe is None:
            return

        self.running = True

        total_seconds = recipe.cooking_time * 60
        start_time = time.time()

        self.timer_status.value = "Cooking..."
        self.start_button.bgcolor = "#374151"
        self.stop_button.bgcolor = "#DC2626"
        self.page.update()

        self.page.run_task(self.update_timer, total_seconds, start_time)

    def stop(self):
        self.running = False
        self.timer_status.value = "Stopped"
        self.start_button.bgcolor = "#FFFFFF"
        self.stop_button.bgcolor = "#374151"
        self.page.update()

    async def update_timer(self, total_seconds, start_time):
        while self.running:
            elapsed = time.time() - start_time
            progress = elapsed / total_seconds

            if progress >= 1:
                self.running = False
                self.timer_text.value = "00:00"
                self.timer_status.value = "Done"
                self.start_button.bgcolor = "#FFFFFF"
                self.stop_button.bgcolor = "#374151"
                self.page.update()
                return

            remaining = int(total_seconds - elapsed)
            minutes = remaining // 60
            seconds = remaining % 60

            self.timer_text.value = f"{minutes:02d}:{seconds:02d}"
            self.timer_status.value = "Cooking..."
            self.page.update()

            await asyncio.sleep(0.1)