#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define all(c) c.begin(), c.end()
#define vvi vector<vector<int>>
#define vvc vector<vector<char>>
#define vi vector<int>
#define vc vector<char>
#define vll vector<long long>
#define vvll vector<vector<long long>>
using namespace std;

vvc grid(45, vc(45));
vector<string> not_found, found_words;

bool find_horizontal(int x, int y, string word)
{
  string word_got;
  for (int i = 0; i < word.size(); i++)
  {
    if (y + i < 0 || y + i >= 45)
      break;
    word_got.push_back(grid[x][y + i]);
  }

  if (word_got == word)
  {
    for (int i = 0; i < word.size(); i++)
    {
      if (y + i < 0 || y + i >= 45)
        break;
      grid[x][y + i] = '-';
    }
    return true;
  }

  word_got.clear();
  for (int i = 0; i < word.size(); i++)
  {
    if (y - i < 0 || y - i >= 45)
      break;
    word_got.push_back(grid[x][y - i]);
  }
  if (word_got == word)
  {
    for (int i = 0; i < word.size(); i++)
    {
      if (y - i < 0 || y - i >= 45)
        break;
      grid[x][y - i] = '-';
    }
    return true;
  }
  return false;
}

bool find_vertical(int x, int y, string word)
{
  string word_got;
  for (int i = 0; i < word.size(); i++)
  {
    if (x + i < 0 || x + i >= 45)
      break;
    word_got.push_back(grid[x + i][y]);
  }

  if (word_got == word)
  {
    for (int i = 0; i < word.size(); i++)
    {
      if (x + i < 0 || x + i >= 45)
        break;
      grid[x + i][y] = '-';
    }
    return true;
  }

  word_got.clear();
  for (int i = 0; i < word.size(); i++)
  {
    if (x - i < 0 || x - i >= 45)
      break;
    word_got.push_back(grid[x - i][y]);
  }
  if (word_got == word)
  {
    for (int i = 0; i < word.size(); i++)
    {
      if (x - i < 0 || x - i >= 45)
        break;
      grid[x - i][y] = '-';
    }
    return true;
  }
  return false;
}

bool find_diagonal(int x, int y, string word)
{
  string word_got;

  for (int i = 0; i < word.size(); i++)
  {
    if (x + i >= 45 || y + i >= 45)
      break;
    word_got.push_back(grid[x + i][y + i]);
  }

  if (word_got == word)
  {
    for (int i = 0; i < word.size(); i++)
    {
      if (x + i >= 45 || y + i >= 45)
        break;
      grid[x + i][y + i] = '-';
    }
    return true;
  }

  word_got.clear();
  for (int i = 0; i < word.size(); i++)
  {
    if (x - i < 0 || y - i < 0)
      break;
    word_got.push_back(grid[x - i][y - i]);
  }
  if (word_got == word)
  {
    for (int i = 0; i < word.size(); i++)
    {
      if (x - i < 0 || y - i < 0)
        break;
      grid[x - i][y - i] = '-';
    }
    return true;
  }

  word_got.clear();
  for (int i = 0; i < word.size(); i++)
  {
    if (x - i < 0 || y + i >= 45)
      break;
    word_got.push_back(grid[x - i][y + i]);
  }
  if (word_got == word)
  {
    for (int i = 0; i < word.size(); i++)
    {
      if (x - i < 0 || y + i >= 45)
        break;
      grid[x - i][y + i] = '-';
    }
    return true;
  }

  word_got.clear();
  for (int i = 0; i < word.size(); i++)
  {
    if (x + i >= 45 || y - i < 0)
      break;
    word_got.push_back(grid[x + i][y - i]);
  }
  if (word_got == word)
  {
    for (int i = 0; i < word.size(); i++)
    {
      if (x + i >= 45 || y - i < 0)
        break;
      grid[x + i][y - i] = '-';
    }
    return true;
  }

  return false;
}

bool find_L_pattern(int x, int y, string word)
{
  int n = word.size();
  string reversed_word = word;
  reverse(reversed_word.begin(), reversed_word.end());

  // up -> right
  for (int k = 1; k <= n; k++)
  {
    string word_got;

    if (x - k + 1 < 0)
    {
      continue;
    }
    for (int i = 0; i < k; i++)
    {
      word_got.push_back(grid[x - i][y]);
    }

    if (y + n - k >= 45)
    {
      continue;
    }
    for (int i = k + 1; i < n + 1; i++)
    {
      word_got.push_back(grid[x - k + 1][y + i - k]);
    }
    //cout << word_got << ",";
    if (word_got == word || word_got == reversed_word)
    {
      for (int i = 0; i < k; i++)
      {
        grid[x - i][y] = '-';
      }
      for (int i = k; i < n+1; i++)
      {
        grid[x - k + 1][y + i - k] = '-';
      }
      return true;
    }
  }

  // down -> right
  for (int k = 1; k <= n; k++)
  {
    string word_got;

    if (x + k - 1 >= 45)
    {
      continue;
    }
    for (int i = 0; i < k; i++)
    {
      word_got.push_back(grid[x + i][y]);
    }

    if (y + n - k >= 45)
    {
      continue;
    }
    for (int i = k + 1; i < n + 1; i++)
    {
      word_got.push_back(grid[x + k - 1][y + i - k]);
    }

    if (word_got == word || word_got == reversed_word)
    {
      for (int i = 0; i < k; i++)
      {
        grid[x + i][y] = '-';
      }
      for (int i = k; i < n+1; i++)
      {
        grid[x + k - 1][y + i - k] = '-';
      }
      return true;
    }
  }

  // right -> up
  for (int k = 1; k <= n; k++)
  {
    string word_got;

    if (y + k - 1 >= 45)
    {
      continue;
    }
    for (int i = 0; i < k; i++)
    {
      word_got.push_back(grid[x][y + i]);
    }

    if (x - n + k < 0)
    {
      continue;
    }
    for (int i = k + 1; i < n + 1; i++)
    {
      word_got.push_back(grid[x - i + k][y + k - 1]);
    }

    if (word_got == word || word_got == reversed_word)
    {
      for (int i = 0; i < k; i++)
      {
        grid[x][y + i] = '-';
      }
      for (int i = k; i < n+1; i++)
      {
        grid[x - i + k][y + k - 1] = '-';
      }
      return true;
    }
  }

  // right -> down
  for (int k = 1; k <= n; k++)
  {
    string word_got;

    if (y + k - 1 >= 45)
    {
      continue;
    }
    for (int i = 0; i < k; i++)
    {
      word_got.push_back(grid[x][y + i]);
    }

    if (x + n - k >= 45)
    {
      continue;
    }
    for (int i = k + 1; i < n + 1; i++)
    {
      word_got.push_back(grid[x + i - k][y + k - 1]);
    }

    if (word_got == word || word_got == reversed_word)
    {
      for (int i = 0; i < k; i++)
      {
        grid[x][y + i] = '-';
      }
      for (int i = k; i < n+1; i++)
      {
        grid[x + i - k][y + k - 1] = '-';
      }
      return true;
    }
  }

  return false;
}

string get_final_chars(){
  string password;
  for (auto row : grid)
  {
    for (auto x : row)
    {
      if (x != '-') {
        password.push_back(x);
      }
    }
  }
  return password;
}

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  vector<string> words(150);
  ll words_total_char;

  for (auto &row : grid)
  {
    for (auto &x : row)
    {
      cin >> x;
    }
  }

  for (auto &word : words)
  {
    cin >> word;
    words_total_char += word.size();
  }

  for (auto word : words)
  {
    bool found = false;
    for (int i = 0; i < 45; i++)
    {
      for (int j = 0; j < 45; j++)
      {
        if (find_horizontal(i, j, word) 
          || find_vertical(i, j, word) 
          || find_diagonal(i, j, word) 
          || find_L_pattern(i, j, word)
        ){
          found = true;
          found_words.push_back(word);
        }else{
          not_found.push_back(word);
        }
      }
    }
    if (!found)
    {
      //cout << "Not found " << word << "\n";
    }
  }

  for (auto row : grid)
  {
    for (auto x : row)
    {
      cout << x << " ";
    }
    cout << endl;
  }

  ll total_found = 0;
  for (auto word : found_words)
  {
    total_found += word.size();
  }

  cout << "Total words found:" << endl;
  cout << found_words.size() << endl;

  cout << "Total characters found:" << endl;
  cout << total_found << endl;

  string res = get_final_chars();
  cout << "Total characters deleted from grid:" << endl;
  cout << 45*45 - res.size() << endl;
  cout << "Password("<< res.size() << "): \n";
  cout << res << endl;

  return 0;
}
