#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>

class StoppingGame {
 public:
  StoppingGame(int boxes, int rewards, double reward_value, double opening_cost = 1.0)
      : boxes_(boxes), rewards_(rewards), reward_value_(reward_value), opening_cost_(opening_cost) {
    if (boxes_ <= 0 || rewards_ < 0 || rewards_ > boxes_ || reward_value_ < 0.0 || opening_cost_ < 0.0) {
      throw std::invalid_argument("invalid game parameters");
    }
    memo_.assign(rewards_ + 1, std::vector<double>(boxes_ - rewards_ + 1, std::numeric_limits<double>::quiet_NaN()));
  }

  // Maximum expected gain available after x rewards and y empty boxes have
  // been observed. Stopping has value zero, so the value is never negative.
  double value(int x = 0, int y = 0) {
    if (x == rewards_ || x + y == boxes_) {
      return 0.0;
    }

    double& cached = memo_.at(x).at(y);
    if (!std::isnan(cached)) {
      return cached;
    }

    const double unopened = boxes_ - x - y;
    const double reward_probability = (rewards_ - x) / unopened;
    const double reward_successor = reward_probability > 0.0 ? value(x + 1, y) : 0.0;
    const double empty_successor = reward_probability < 1.0 ? value(x, y + 1) : 0.0;
    const double continue_value =
        reward_probability * (reward_value_ - opening_cost_ + reward_successor) +
        (1.0 - reward_probability) * (-opening_cost_ + empty_successor);

    cached = std::max(0.0, continue_value);
    return cached;
  }

  bool should_continue(int x, int y) {
    if (x == rewards_ || x + y == boxes_) {
      return false;
    }
    const double unopened = boxes_ - x - y;
    const double reward_probability = (rewards_ - x) / unopened;
    const double reward_successor = reward_probability > 0.0 ? value(x + 1, y) : 0.0;
    const double empty_successor = reward_probability < 1.0 ? value(x, y + 1) : 0.0;
    const double continue_value =
        reward_probability * (reward_value_ - opening_cost_ + reward_successor) +
        (1.0 - reward_probability) * (-opening_cost_ + empty_successor);
    return continue_value > 0.0;
  }

 private:
  int boxes_;
  int rewards_;
  double reward_value_;
  double opening_cost_;
  std::vector<std::vector<double>> memo_;
};

int main() {
  StoppingGame game(/*boxes=*/20, /*rewards=*/5, /*reward_value=*/5.0);
  std::cout << std::fixed << std::setprecision(10) << game.value() << '\n';
  return 0;
}
