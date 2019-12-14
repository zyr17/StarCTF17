#include <bits/stdc++.h>

int flaground[] = {30, 70, 101};
char buffer[1111111];

FILE *logfile;

void log(char *ch){
    fprintf(logfile, "%s", ch);
    fflush(logfile);
    fprintf(stderr, "|%s|\n", ch);
}

#define N 111111

int n, m, K;
long long d[N][11];
bool in[N][11];
std::vector<std::pair<int, int>> edge[N];

long long solve1(){
    memset(d, 63, sizeof d);
    memset(in, 0, sizeof in);
    d[1][0] = 0;
    std::vector<std::pair<int, int>> line;
    line.push_back(std::make_pair(1, 0));
    long long res = 9999999999999999LL;
    for (int L = 0; L < line.size(); L ++ ){
        int i = line[L].first, j = line[L].second;
        for (auto k : edge[i]){
            if (j < K && d[i][j] < d[k.first][j + 1]){
                d[k.first][j + 1] = d[i][j];
                if (!in[k.first][j + 1]){
                    in[k.first][j + 1] = 1;
                    line.push_back(std::make_pair(k.first, j + 1));
                }
            }
            if (d[i][j] + k.second < d[k.first][j]){
                d[k.first][j] = d[i][j] + k.second;
                if (!in[k.first][j]){
                    in[k.first][j] = 1;
                    line.push_back(std::make_pair(k.first, j));
                }
            }
            in[i][j] = 0;
        }
        if (i == n && d[i][j] < res)
            res = d[i][j];
    }
    return res;
}

void Main(){
    std::cin >> n >> m >> K;
    std::cerr << n << ' ' << m << ' ' << K << std::endl;
    for (int i = 1; i <= n; i ++ )
        edge[i].clear();
    for (int i = 1; i <= m; i ++ ){
        int t1, t2, t3;
        std::cin >> t1 >> t2 >> t3;
        edge[t1].push_back(std::make_pair(t2, t3));
        edge[t2].push_back(std::make_pair(t1, t3));
    }
    long long res = solve1();
    std::cout << res << std::endl;
}

int main(){
    fprintf(stderr, "hello");
    logfile = fopen("flight.out", "w");
    gets(buffer);
    gets(buffer);
    gets(buffer);
    int nowflag = 0;
    for (int i = 1; i <= 999; i ++ ){
        fprintf(stderr, "%d\n", i);
        Main();
        if (i == flaground[nowflag]){
            getchar();
            gets(buffer);
            log(buffer);
            nowflag ++ ;
        }
    }
}