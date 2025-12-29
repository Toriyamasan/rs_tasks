#!/bin/bash
# SPDX-FileCopyrightText: 2025 Toriyamasan
# SPDX-License-Identifier: GPL-3.0-only

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

res=0

timeout 15 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

if ! grep -q 'rad' /tmp/mypkg.log; then
    echo "テスト失敗: rad の出力が見つかりません"
    res=1
fi

if ! grep -q '0.2618' /tmp/mypkg.log; then
    echo "テスト失敗: 15度に対する計算結果(0.2618 rad)が正しくありません"
    res=1
fi

if [ "${res}" = 0 ]; then
    echo "すべてのテストに合格しました (OK)"
else
    echo "テストのどこかでエラーが発生しました"
fi

exit $res
