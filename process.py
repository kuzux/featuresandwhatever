#!/usr/bin/env python

import pandas as pd
import numpy as np

#requires the following libraries: numpy and pandas

# handle each acc-gyro couple for a user-location pairing
def handle_couple(acc_name, gyro_name):
    #read the data from csv
    acc = pd.read_csv(acc_name)
    gyro = pd.read_csv(gyro_name)

    # calculate magnitudes
    acc["MAG"] = np.sqrt(acc["V1"]**2 + acc["V2"]**2 + acc["V3"]**2)
    gyro["MAG"] = np.sqrt(gyro["V1"]**2 + gyro["V2"]**2 + gyro["V3"]**2)

    idcol = []

    # Acc feature columns
    meanax = []
    meanay = []
    meanaz = []
    meanamag = []
    minax = []
    minay = []
    minaz = []
    minamag = []
    maxax = []
    maxay = []
    maxaz = []
    maxamag = []
    varax = []
    varay = []
    varaz = []
    varamag = []

    # Gyro feature columns
    meangx = []
    meangy = []
    meangz = []
    meangmag = []
    mingx = []
    mingy = []
    mingz = []
    mingmag = []
    maxgx = []
    maxgy = []
    maxgz = []
    maxgmag = []
    vargx = []
    vargy = []
    vargz = []
    vargmag = []

    zcrax = []
    zcray = []
    zcraz = []
    zcramag =[]

    zcrgx = []
    zcrgy = []
    zcrgz = []
    zcrgmag =[]

    loc = []
    act = []

    # 2 seconds in 100Hz = 200 rows for each 2 second sample
    # (might be a bit of a problem if we're dealing with faulty data)
    for idx in range(0, min(len(acc), len(gyro)), 200):
        sample_acc = acc[idx:idx+200]
        sample_gyro = gyro[idx:idx+200]

        idcol = sample_acc["ID"].iloc[0]


        # calculate each feature from that
        meanax.append(sample_acc["V1"].mean())
        meanay.append(sample_acc["V2"].mean())
        meanaz.append(sample_acc["V3"].mean())
        meanamag.append(sample_acc["MAG"].mean())

        minax.append(sample_acc["V1"].min())
        minay.append(sample_acc["V2"].min())
        minaz.append(sample_acc["V3"].min())
        minamag.append(sample_acc["MAG"].min())

        maxax.append(sample_acc["V1"].max())
        maxay.append(sample_acc["V2"].max())
        maxaz.append(sample_acc["V3"].max())
        maxamag.append(sample_acc["MAG"].max())

        varax.append(sample_acc["V1"].var())
        varay.append(sample_acc["V2"].var())
        varaz.append(sample_acc["V3"].var())
        varamag.append(sample_acc["MAG"].var())

        meangx.append(sample_gyro["V1"].mean())
        meangy.append(sample_gyro["V2"].mean())
        meangz.append(sample_gyro["V3"].mean())
        meangmag.append(sample_gyro["MAG"].mean())

        mingx.append(sample_gyro["V1"].min())
        mingy.append(sample_gyro["V2"].min())
        mingz.append(sample_gyro["V3"].min())
        mingmag.append(sample_gyro["MAG"].min())

        maxgx.append(sample_gyro["V1"].max())
        maxgy.append(sample_gyro["V2"].max())
        maxgz.append(sample_gyro["V3"].max())
        maxgmag.append(sample_gyro["MAG"].max())

        vargx.append(sample_gyro["V1"].var())
        vargy.append(sample_gyro["V2"].var())
        vargz.append(sample_gyro["V3"].var())
        vargmag.append(sample_gyro["MAG"].var())

        loc.append(sample_acc["LOC"].iloc[0])
        act.append(sample_acc["ACT"].iloc[0])

        zcrax.append(len(np.where(np.diff(np.signbit(np.subtract(sample_acc["V1"], sample_acc["V1"].mean()))))[0]))
        zcray.append(len(np.where(np.diff(np.signbit(np.subtract(sample_acc["V2"], sample_acc["V2"].mean()))))[0]))
        zcraz.append(len(np.where(np.diff(np.signbit(np.subtract(sample_acc["V3"], sample_acc["V3"].mean()))))[0]))
        zcramag.append(len(np.where(np.diff(np.signbit(np.subtract(sample_acc["MAG"], sample_acc["MAG"].mean()))))[0]))

        zcrgx.append(len(np.where(np.diff(np.signbit(np.subtract(sample_gyro["V1"], sample_gyro["V1"].mean()))))[0]))
        zcrgy.append(len(np.where(np.diff(np.signbit(np.subtract(sample_gyro["V2"], sample_gyro["V2"].mean()))))[0]))
        zcrgz.append(len(np.where(np.diff(np.signbit(np.subtract(sample_gyro["V3"], sample_gyro["V3"].mean()))))[0]))
        zcrgmag.append(len(np.where(np.diff(np.signbit(np.subtract(sample_gyro["MAG"], sample_gyro["MAG"].mean()))))[0]))

    # convert the feature columns into a DataFrame to be later output as a csv file
    res = pd.DataFrame({ 'ID': idcol, 

        'MEANAX': meanax,
        'MEANAY': meanay,
        'MEANAZ': meanaz,
        'MEANAMAG': meanamag,
        'MINAX': minax,
        'MINAY': minay,
        'MINAZ': minaz,
        'MINAMAG': minamag,
        'MAXAX': maxax,
        'MAXAY': maxay,
        'MAXAZ': maxaz,
        'MAXAMAG': maxamag,
        'VARAX': varax,
        'VARAY': varay,
        'VARAZ': varaz,
        'VARAMAG': varamag,
        'ZCRAX': zcrax,
        'ZCRAY': zcray,
        'ZCRAZ': zcraz,
        'ZCRAMAG': zcramag,

        'MEANGX': meangx,
        'MEANGY': meangy,
        'MEANGZ': meangz,
        'MEANGMAG': meangmag,
        'MINGX': mingx,
        'MINGY': mingy,
        'MINGZ': mingz,
        'MINGMAG': mingmag,
        'MAXGX': maxgx,
        'MAXGY': maxgy,
        'MAXGZ': maxaz,
        'MAXGMAG': maxgmag,
        'VARGX': vargx,
        'VARGY': vargy,
        'VARGZ': vargz,
        'VARGMAG': vargmag,
        'ZCRGX': zcrgx,
        'ZCRGY': zcrgy,
        'ZCRGZ': zcrgz,
        'ZCRGMAG': zcrgmag,

        'LOC': loc,
        'ACT': act
    })

    return res

# for each user, calculate all the acc-gyro pairs and concat them to a single csv file
def handle_user(couples, outfile):
    total = None

    for couple in couples:
        if total is None:
            total = handle_couple(couple[0], couple[1])
        else:
            total = pd.concat([total, handle_couple(couple[0], couple[1])])

    # write the computed csv file out
    total.to_csv(outfile, index=False)

# for all users list
def handle_users(users):
    for user in users:
        handle_user(user[0], user[1])

# generating user filenames

users = []

for i in range(1, 16):
    bag_acc = "Bag/acc%d.csv" % (i, )
    bag_gyro = "Bag/gyro%d.csv" % (i, )
    hand_acc = "Hand/acc%d.csv" % (i, )
    hand_gyro = "Hand/gyro%d.csv" % (i, )
    pocket_acc = "Pocket/acc%d.csv" % (i, )
    pocket_gyro = "Pocket/gyro%d.csv" % (i, )

    out = "user%d.csv" % (i, )
    users.append(([(bag_acc, bag_gyro), (hand_acc, hand_gyro), (pocket_acc, pocket_gyro)], out))

handle_users(users)
