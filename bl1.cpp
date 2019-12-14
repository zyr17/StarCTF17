#include <bits/stdc++.h>

int flaground[] = {30, 70, 101};

char buffer[666666];
long long d[100][222];

struct Point{
    long long x, y;
    double cmpnum;
    Point(){}
    Point(long long x, long long y) : x(x), y(y) {
        cmpnum = 0;
        if (x < 0 && y >= 0) cmpnum = 1;
        if (x <= 0 && y < 0) cmpnum = 2;
        if (x > 0 && y <= 0) cmpnum = 3;
        cmpnum = cmpnum * 10 + atan2(y, x);
    }
    bool operator< (Point k){
        return cmpnum < k.cmpnum;
    }
    long long cross(Point k){
        return x * k.y - y * k.x;
    }
    long long operator* (Point k){
        return x * k.x + y * k.y;
    }
    double len(){
        return std::sqrt(x * x + y * y);
    }
};

FILE *logfile;

void log(char *ch){
    fprintf(logfile, "%s", ch);
    fflush(logfile);
    fprintf(stderr, "|%s|\n", ch);
}

long long sqsize(Point i, Point j, Point k, Point l){
    return std::abs(i.cross(j) + j.cross(k) + k.cross(l) + l.cross(i));
}

long long naive(std::vector<Point> points){
    long long res = 0;
    for (auto i : points)
        for (auto j : points)
            for (auto k : points)
                for (auto l : points){
                    long long now = sqsize(i, j, k, l);
                    if (now > res) {res = now;std::cout << i.x << ' ' << i.y << ',' << j.x << ' ' << j.y << ',' << k.x << ' ' << k.y << ',' << l.x << ' ' << l.y << '\n';}
                }
    return res;
}

std::vector<Point> convex(std::vector<Point> points){
    int minx = 0;
    for (int i = 0; i < points.size(); i ++ )
        if (points[i].x < points[minx].x || points[i].x == points[minx].x && points[i].y < points[minx].y)
            minx = i;
    std::vector<Point> res;
    for (int ii = 0; ii < points.size(); ii ++ ){
        auto i = points[(ii + minx) % points.size()];
        for (; res.size() > 1; ){
            Point &base = res[res.size() - 2];
            Point nowv = Point(res[res.size() - 1].x - base.x, res[res.size() - 1].y - base.y);
            Point newv = Point(i.x - base.x, i.y - base.y);
            if (nowv.cross(newv) <= 0) res.pop_back();
            else break;
        }
        res.push_back(i);
    }
    return res;
}

long long ad1(std::vector<Point> points){
    points = convex(points);
    long long res = 0;
    for (int ii = 0; ii < points.size(); ii ++ ){
        int kk = ii + 1, ll = ii + 3;
        for (int jj = ii + 2; jj < points.size() - 1; jj ++ ){
            auto &i = points[ii], &j = points[jj];
            long long x, y;
            x = i.y - j.y;
            y = j.x - i.x;
            if (!(x || y)) continue;
            Point pp(x, y);

            for (; ; ){
                long long nows = std::abs(pp * Point(points[kk].x - i.x, points[kk].y - i.y));
                int nk = (kk + 1) % points.size();
                long long nexts = std::abs(pp * Point(points[nk].x - i.x, points[nk].y - i.y));
                if (nexts > nows) kk = nk;
                else break;
            }
            for (; ; ){
                long long nows = std::abs(pp * Point(points[ll].x - i.x, points[ll].y - i.y));
                int nl = (ll + 1) % points.size();
                long long nexts = std::abs(pp * Point(points[nl].x - i.x, points[nl].y - i.y));
                if (nexts > nows) ll = nl;
                else break;
            }
            //std::cout << i.x << ' ' << i.y << '|' << j.x << ' ' << j.y << '|' << mini.x << ' ' << mini.y << '|' << maxi.x << ' ' << maxi.y << '\n';
            long long now = sqsize(i, points[kk], j, points[ll]);
            //std::cout << ii << ' ' << jj << ' ' << kk << ' ' << ll << ' ' << now << std::endl;
            if (res < now) res = now;
        }
    }
    return res;
}

void Main(){
    long long n;
    std::cin >> n;
    fprintf(stderr, "%lld\n", n); fflush(stderr);
    fprintf(logfile, "%lld\n", n); fflush(logfile);
    std::vector<Point> points;
    for (int i = 0; i < n; i ++ ){
        long long x, y;
        std::cin >> x >> y;
        points.push_back(Point(x, y));
        fprintf(logfile, "%d %d\n", x, y); fflush(logfile);
    }
    std::sort(points.begin(), points.end());
    long long res, cres;
    //cres = naive(points);
    res = ad1(points);
    //if (cres != res) fprintf(stderr, "%lld %lld\n", cres, res); fflush(stderr);
    std::cout << res / 2 << (res % 2 ? ".5" : ".0") << std::endl;
}

int main(){
    fprintf(stderr, "hello");
    logfile = fopen("bl1.out", "w");
    gets(buffer);
    gets(buffer);
    int nowflag = 0;
    for (int i = 1; i <= 109; i ++ ){
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