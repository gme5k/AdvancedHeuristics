 g, (ax1) = plt.subplots(1)
    if doubleBranch == 1:
        ax1.scatter(q0l, iterl2, color = "red")
        
    ax1.set_title("1/2")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    plt.savefig('plots/1-2.png', bbox_inches='tight')
    
    h, (ax1) = plt.subplots(1)
    ax1.scatter(q1l, iterl, color = "black")
    
    if doubleBranch == 1:
        ax1.scatter(q1l, iterl2, color = "red")
    ax1.set_title("2/3")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    
    plt.savefig('plots/2-3.png', bbox_inches='tight')

    i, (ax1) = plt.subplots(1)
    ax1.scatter(q2l, iterl, color = "black")

    if doubleBranch == 1:
        ax1.scatter(q2l, iterl2, color = "red")
    ax1.set_title("3/4")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    
    plt.savefig('plots/3-4.png', bbox_inches='tight')

    j, (ax1) = plt.subplots(1)
    ax1.scatter(q3l, iterl, color = "black")

    if doubleBranch == 1:
        ax1.scatter(q3l, iterl2, color = "red")
    ax1.set_title("4/5")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    
    plt.savefig('plots/4-5.png', bbox_inches='tight')

    k, (ax1) = plt.subplots(1)
    ax1.scatter(q4l, iterl, color = "black")

    if doubleBranch == 1:
        ax1.scatter(q4l, iterl2, color = "red")
    ax1.set_title("5/6")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    
    plt.savefig('plots/5-6.png', bbox_inches='tight')

    l, (ax1) = plt.subplots(1)
    ax1.scatter(q5l, iterl, color = "black")

    if doubleBranch == 1:
        ax1.scatter(q5l, iterl2, color = "red")
    ax1.set_title("6/7")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    
    plt.savefig('plots/6-7.png', bbox_inches='tight')
#~ ____________________________________________________________________-
    m, (ax1) = plt.subplots(1)
    ax1.scatter(sDevl, iterl, color = "black")
 
    if doubleBranch == 1:
        ax1.scatter(sDevl, iterl2, color = "red")
    ax1.set_title("sDev")
    ax1.set_xlabel("SDev", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    
    plt.savefig('plots/sDev.png', bbox_inches='tight')

    n, (ax1) = plt.subplots(1)
    ax1.scatter(avgl, scorel, color = "black")

    if doubleBranch == 1:
        ax1.scatter(avgl, iterl2, color = "red")
    ax1.set_title("average cost/lowest score")
    ax1.set_xlabel("avg cost", fontsize = 26)
    ax1.set_ylabel("lowest score", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    plt.savefig('plots/avg.png', bbox_inches='tight')

#~ ____________________________________________________________________-
    o, (ax1) = plt.subplots(1)
    ax1.scatter(q0l, iterl, color = "black")

    if doubleBranch == 1:
        ax1.scatter(q0l, iterl2, color = "red")
    ax1.set_title("1/2")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    ax1.set_yscale('log')
    plt.savefig('plots/1-2-log.png', bbox_inches='tight')

    p, (ax1) = plt.subplots(1)
    ax1.scatter(q1l, iterl, color = "black")
  
    if doubleBranch == 1:
        ax1.scatter(q1l, iterl2, color = "red")
    ax1.set_title("2/3")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    ax1.set_yscale('log')
    plt.savefig('plots/2-3-log.png', bbox_inches='tight')

    q, (ax1) = plt.subplots(1)
    ax1.scatter(q2l, iterl, color = "black")

    if doubleBranch == 1:
        ax1.scatter(q2l, iterl2, color = "red")
    ax1.set_title("3/4")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    ax1.set_yscale('log')
    plt.savefig('plots/3-4-log.png', bbox_inches='tight')

    r, (ax1) = plt.subplots(1)
    ax1.scatter(q3l, iterl, color = "black")

    if doubleBranch == 1:
        ax1.scatter(q3l, iterl2, color = "red")
    ax1.set_title("4/5")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    ax1.set_yscale('log')
    plt.savefig('plots/4-5-log.png', bbox_inches='tight')

    s, (ax1) = plt.subplots(1)
    ax1.scatter(q4l, iterl, color = "black")
 
    if doubleBranch == 1:
        ax1.scatter(q4l, iterl2, color = "red")
    ax1.set_title("5/6")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    ax1.set_yscale('log')
    plt.savefig('plots/5-6-log.png', bbox_inches='tight')

    t, (ax1) = plt.subplots(1)
    ax1.scatter(q5l, iterl, color = "black")

    if doubleBranch == 1:
        ax1.scatter(q5l, iterl2, color = "red")
    ax1.set_title("6/7")
    ax1.set_xlabel("difference", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    ax1.set_yscale('log')
    plt.savefig('plots/6-7-log.png', bbox_inches='tight')
#~ ____________________________________________________________________-
    u, (ax1) = plt.subplots(1)
    ax1.scatter(sDevl, iterl, color = "black")

    if doubleBranch == 1:
        ax1.scatter(sDevl, iterl2, color = "red")
    ax1.set_title("sDev")
    ax1.set_xlabel("SDev", fontsize = 26)
    ax1.set_ylabel("iterations", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    ax1.set_yscale('log')
    plt.savefig('plots/sDev-log.png', bbox_inches='tight')
    
    v, (ax1) = plt.subplots(1)
    ax1.scatter(avgl, scorel, color = "black")

    if doubleBranch == 1:
        ax1.scatter(avgl, iterl2, color = "red")
    ax1.set_title("average cost/lowest score")
    ax1.set_xlabel("avg cost", fontsize = 26)
    ax1.set_ylabel("lowest score", fontsize = 24)
    ax1.tick_params(labelsize = 18)
    ax1.set_yscale('log')
    plt.savefig('plots/avg-log.png', bbox_inches='tight')
