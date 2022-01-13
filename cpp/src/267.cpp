#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>

unsigned int getMinHeads(unsigned int tosses, double billion, double step = 0.0001)
{
  unsigned int result = tosses;

  for (double ratio = 0; ratio < 1; ratio += step)
  {
    auto won  = 1 + 2 * ratio;
    auto lost = 1 - ratio;

    unsigned int heads = result;
    for (; heads > 0; heads--)
    {
      auto total = pow(won, heads) * pow(lost, tosses - heads);
      if (total < billion)
      {
        heads++;
        break;
      }
    }

    if (result > heads)
      result = heads;
  }

  return result;
}

double probability(unsigned int minHeads, unsigned int maxTosses, unsigned int tosses = 0, unsigned int heads = 0)
{
  if (heads >= minHeads)
    return 1;
  if (maxTosses - tosses < minHeads - heads)
    return 0;

  const double Unknown = -1;
  static std::vector<double> cache(minHeads*maxTosses, Unknown);
  auto id = heads * maxTosses + tosses;
  if (cache[id] != Unknown)
    return cache[id];

  auto result = 0.5 * probability(minHeads, maxTosses, tosses + 1, heads + 1) +
                0.5 * probability(minHeads, maxTosses, tosses + 1, heads    );

  cache[id] = result;
  return result;
}

int main()
{
  unsigned int tosses = 1000;
  double money = 1000000000;

  std::cin >> tosses >> money;

  auto minHeads = getMinHeads(tosses, money);

  std::cout << std::fixed << std::setprecision(12)
            << probability(minHeads, tosses) << std::endl;
  return 0;
}
