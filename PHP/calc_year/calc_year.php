<!-- 未入力・誤入力 対応がまだ-->

<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>result/年計算アプリ</title>
</head>

<body>
    <?php
    // var_dump($_POST);
    $ge = $_POST['val'];
    $y_bir = $_POST['num_y'];
    $month = $_POST['num_m'];

    // 元号で入力した場合、西暦を計算する
    if ($ge == 'm') {
        if ($y_bir == 1 or $y_bir == '元') {
            $y_bir = '元';
            $year = 1868;
        } else {
            $year = $y_bir + 1867;
        }
        $gen = '明治';
    } else if ($ge == 't') {
        if ($y_bir == 1 or $y_bir == '元') {
            $y_bir = '元';
            $year = 1912;
        } else {
            $year = $y_bir + 1911;
        }
        $gen = '大正';
    } else if ($ge == 's') {
        if ($y_bir == 1 or $y_bir == '元') {
            $y_bir = '元';
            $year = 1926;
        } else {
            $year = $y_bir + 1925;
        }
        $gen = '昭和';
    } else if ($ge == 'h') {
        if ($y_bir == 1 or $y_bir == '元') {
            $y_bir = '元';
            $year = 1989;
        } else {
            $year = $y_bir + 1988;
        }
        $gen = '平成';
    } else if ($ge == 'r') {
        if ($y_bir == 1 or $y_bir == '元') {
            $y_bir = '元';
            $year = 2019;
        } else {
            $year = $y_bir + 2018;
        }
        $gen = '令和';
    } else {
        // 西暦入力の場合、元号を計算する
        $year = $y_bir;
        if ($year >= 2019) {
            $gen = '令和';
            if ($year == 2019) {
                $y_bir = '元';
            } else {
                $y_bir = $year - 2018;
            }
        } else if ($year >= 1989) {
            $gen = '平成';
            if ($year == 1989) {
                $y_bir = '元';
            } else {
                $y_bir = $year - 1988;
            }
        } else if ($year >= 1926) {
            $gen = '昭和';
            if ($year == 1926) {
                $y_bir = '元';
            } else {
                $y_bir = $year - 1925;
            }
        } else if ($year >= 1912) {
            $gen = '大正';
            if ($year == 1912) {
                $y_bir = '元';
            } else {
                $y_bir = $year - 1911;
            }
        } else if ($year >= 1868) {
            $gen = '明治';
            if ($year == 1868) {
                $y_bir = '元';
            } else {
                $y_bir = $year - 1867;
            }
        }
    }

    // 入学年度を計算
    // 1,2,3月生まれは微調整, 4~12月はそのまま足し算
    if ($month >= 4) {
        $y_ele = $year + 7;
        $y_jh = $year + 13;
        $y_h = $year + 16;
        $y_c = $year + 19;
        $y_end = $year + 23;
    } else {
        $y_ele = $year + 6;
        $y_jh = $year + 12;
        $y_h = $year + 15;
        $y_c = $year + 18;
        $y_end = $year + 22;
    }

    $y_l = [$y_ele, $y_jh, $y_h, $y_c, $y_end];
    $y = ['', '', '', '', ''];

    // 各西暦を元号に調整
    for ($i = 0; $i < 5; $i++) {
        if ($y_l[$i] >= 2019) {
            if ($y_l[$i] == 2019) {
                $y[$i] = '令和元';
            } else {
                $dif = $y_l[$i] - 2018;
                $y[$i] = "令和{$dif}";
            }
        } else if ($y_l[$i] >= 1989) {
            if ($y_l[$i] == 1989) {
                $y[$i] = '平成元';
            } else {
                $dif = $y_l[$i] - 1988;
                $y[$i] = "平成{$dif}";
            }
        } else if ($y_l[$i] >= 1926) {
            if ($y_l[$i] == 1926) {
                $y[$i] = '昭和元';
            } else {
                $dif = $y_l[$i] - 1925;
                $y[$i] = "昭和{$dif}";
            }
        } else if ($y_l[$i] >= 1912) {
            if ($y_l[$i] == 1912) {
                $y[$i] = '大正元';
            } else {
                $dif = $y_l[$i] - 1911;
                $y[$i] = "大正{$dif}";
            }
        } else if ($y_l[$i] >= 1868) {
            if ($y_l[$i] == 1868) {
                $y[$i] = '明治元';
            } else {
                $dif = $y_l[$i] - 1867;
                $y[$i] = "明治{$dif}";
            }
        }
    }

    // 出力
    print("<p>{$gen}{$y_bir}年 (西暦 {$year}年) {$month}月 生まれのあなたは</p>");
    print("<p>小学校入学 : {$y[0]}年 (西暦 {$y_ele}年) 4月</p>");
    print("<p>小学校卒業 : {$y[1]}年 (西暦 {$y_jh}年) 3月</p>");
    print("<p>中学校入学 : {$y[1]}年 (西暦 {$y_jh}年) 4月</p>");
    print("<p>中学校卒業 : {$y[2]}年 (西暦 {$y_h}年) 3月</p>");
    print("<p>高校入学 : {$y[2]}年 (西暦 {$y_h}年) 4月</p>");
    print("<p>高校卒業 : {$y[3]}年 (西暦 {$y_c}年) 3月</p>");
    print("<p>大学入学 : {$y[3]}年 (西暦 {$y_c}年) 4月</p>");
    print("<p>大学卒業 : {$y[4]}年 (西暦 {$y_end}年) 3月</p>");
    ?>
</body>

</html>
