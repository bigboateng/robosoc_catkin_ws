import time
class Timer:
  def restart(self):
    self.start = time.time()

  def get_time_secs(self):
    end = time.time()
    return round(end - self.start,2)
