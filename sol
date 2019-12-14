Binary

babyelf:IDA在rodata字段0x708处找到FDUCTF{You_must_know_readelf_strings_or_ida!}
babygdb:IDA把hash函数复制出来执行hash("Welcom to the world of CTF!")得到fductf{554353625620563504665865405}
babypwntools:IDA得到密码为"Welcome","to","paly","CTF","in","sixstars","and","Hack","for","fun"。交互30轮得到FDUCTF{pwnt001s_Is_p0w3rFul}
千王之王:名字buffer28字节，输入28字节名字后会在后面加0导致seed为0。输入28字节名字然后srand(0)即可得到fductf{Every0ne_m4y_be_Stephen_Ch0w}

Crypto

babyRSA:知道epq算出phi逆元得到d, c^d % n = m得到fductf{cee2455ec9b6ace17c1005aeb7d7cb7d}
Crypto-warmup:跑一下得到fductf{welcome_to_the_fductf_to_beat_pow_9f0ecede50ed31fcd982d211e1520786}
commonRSA:n1n2GCD得到p=103440084123937937323529191703891837969326527941420531244604549982744946746913321475619982331436852510887975569547412681214328783131941958217784896524748974755249648095760644197380049022668969288531995346583267798422908632902502845595168841699084553670108617175938883557143168791962943165162625943389478950363。推得fductf{0b461c26f9879c7310869740297234ce}
RdSpA:由于ed % phi = 1, e*(d % (p - 1)) % q - 1 = 1, e*dp-1 = x*q。对e*dp-1分解质因数得到不到512位的数6070702351552426261902745305149300868406236505985454736236488749871676895463474529947965691956194630758400898757033790511875354148837820682891835059351929，枚举倍数并检查倍数+1是否能整除n得到q=12141404703104852523805490610298601736812473011970909472472977499743353790926949059895931383912389261516801797514067581023750708297675641365783670118703859推得fductf{6acff3a7ba451a7476be29ef3c8b7707}
六星福利彩票1:用它给的seed初始化即可得到fductf{known_s3ed_kn0wn_number}
数学作业:抄一下server的代码得到fductf{m@st3r_0f_mOdulu5!}
六星福利彩票2:由于每次位运算均可根据结果逆推，4步逆推得到fductf{go0d_rev3rse_sk1ll!}
宝藏和鹦鹉:鹦鹉会回答6次，其中至多一次说谎。先问每个箱子里是啥，再问任意两个箱子是否相等。如果全部符合事实；一对箱子不符合则结果不变，否则有一个箱子相关的再问都不符合事实，该箱子取反。得到fductf{Aye_ay3_C@ptaIn!}

Misc

变色龙:先cv2取奇数列黑边，然后肉眼观测得到fductf{what_a_colourful_picturE!}
zzzzzip:for i in {2048..1}; do unzip $i; done;得到fductf{an_easy_flag_for_script_baby}
图灵机：根据程序构造得到FDUCTF{4PpLeN0tP35R}
先赚一个小目标：第一天是商品初始价格，每件商品波动范围是[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.5]虽然没去用。每次卖出所有商品并买入低于基准价最多的商品，如果最低高于基准价则只卖不买。多试试得到fductf{Wow_y0u_are_so_capabl3!}

PPC

easyNum:f[i][j]代表i位数字（包括前导0），每位和为j的方案数。为sum(d[i-1][j-9:j-0])。之后求0~(x-1)有几个数和为k，从高位开始枚举，每一位枚举0~(p-1)固定高位，此时低位可以随便填，查表f得到结果。把区间ij拆成calc(j+1)-calc(i)即可。得到fductf{d1GIT_dAn@M1c_Pr09r@mM1N9_15_9u1t3_3@sY!} fductf{DIgit_DaN@M1C_pro9RAMMing_is_quIT3_3@sY!} fductf{tH3_TH1rd_f1@9_1s_dIff3r3NT_w1tH_0th3r5!}
biggestLand:先求凸包。假设凸包点数3个，找一个内部的点让损失面积最小即可（随机出现概率较低多跑几遍就过了没有实现）。否则一定选择凸包上的点。枚举凸包上点x，顺时针枚举其对角点y，可以发现另外两个点ab对于最优解一定也在顺时针转，因此复杂度O(n^2)。实际上随着x转y也必定顺时针，最优可以到O(nlogn)懒得写了。得到fductf{6r33d_i5_9O0d_1F_Y0U_c@n_5urV1V3} fductf{Y3@h!yEAh!1If3_i5_b3@ut1FU1!2eee} fductf{IT_is_g00d_t0_b3_@1iV3,i5N't_iT?}
flight:f[i][j]代表在i用了j块宝石的最低距离。spfa转移。fductf{C@k3_1s_@_j0k3!!cAke_iS_a_70k3!!} fductf{l1f3_i5_A_7Ok3!!L1f3_I5_@_JoKe!!} fdductf{kIng_A&D_6E@r_w0RRy_tH31r_K33p3R}

Web

zc的小秘密-万能密码:`') or 1 = 1 #`得到fductf{err0r_based_inj3ction_Can_get_the_second_fl4g}
Base64:atob('ZmR1Y3Rme2V2M3J5X0NURmVyX2swbndzXzhhc2U2NH0=')=fductf{ev3ry_CTFer_k0nws_8ase64}
天下武功，唯快不破:`$('input').value = eval($('div').innerText.slice(0, $('div').innerText.length - 3)); $('form').submit();`得到fductf{Y0u_Ar3_sO_F4st!}
getfudan:看源码GameManager里http://10.132.141.82/getfudan/在那山的那边海的那边有一群蓝精灵.html 得到base64的fductf{0h_mYYY_6od_yoU_4r3_sO_DaMn_cleee3eeeever!}

代码：https://github.com/zyr17/StarCTF17/tree/19/