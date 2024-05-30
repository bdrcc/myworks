<?php
session_start();

// var_dump($_SESSION['a']);
// var_dump($_SESSION['q']);

if (isset($_SESSION['a']) and isset($_SESSION['q'])) {
    $a = $_SESSION['a'];
    $q = $_SESSION['q'];
    $look_over = $_SESSION['look_over'];

    if (!isset($_GET['finish'])) { // ただ終えた場合
        $title = '解答確認ページ';
    } else {
        $title = '解答一覧ページ';

        $total = 0;
        foreach ($a as $k => $v) {
            if ($v == $q[$k][1]) {
                $total += 10;
            }
        }
        if ($total >= 70) {
            $result = '合格';
        } else {
            $result = '不合格';
        }
    }
} else { // セッションなく初めからこちらに移動した場合
    header('Location:index.php');
    exit();
}


// 本来であれば記述してもいいが、問題を見返す人用にとっておくべき
// session_destroy();
?>

<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php print($title); ?> / 10問クイズ</title>
    <meta name="description" content="3択問題の自分の解答を確認できるページです。">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
</head>

<body>
    <div class="main">
        <?php if (isset($_GET['finish'])) {
            print("<h1>10問クイズ 結果</h1>");
            print("<h2>結果 : {$result}</h2>");
            print("<p>点数 : {$total} 点 / 100 点</p>");
        } else {
            print('<h1>10問クイズ あなたの解答</h1>');
        }
        ?>

        <table class="result">
            <tr>
                <th>問題番号</th>
                <th>あなたの答え</th>
                <?php if (isset($_GET['finish'])) {
                    print('<th>正答</th>');
                } else {
                    print('<th>あとで見る</th>');
                } ?>
            </tr>

            <?php
            $total = 0;
            foreach ($a as $k => $v) {
                $num = $k + 1;
                print("<tr>");
                if (!isset($_GET['finish'])) {
                    print("<td><a href=\"quiz.php?id={$num}&re=on\">{$num}</a></td>");
                } else {
                    print("<td>{$num}</td>");
                }
                print("<td>{$v}</td>");
                if (isset($_GET['finish'])) {
                    if ($v == $q[$k][1]) {
                        print("<td>{$q[$k][1]}</td>");
                    } else {
                        print("<td class='miss'>{$q[$k][1]}</td>");
                    }
                } else {
                    if ($look_over[$k] == 'on') {
                        print("<td><i class=\"fa-solid fa-square-check\"></i></td>");
                    } else {
                        print("<td></td>");
                    }
                }
                print("</tr>");
            }
            ?>
        </table>

        <?php if (!isset($_GET['finish'])) { // ただ終えた場合
            print('<a href="end.php?finish=1" class="back_home small">解答を送信する</a>');
        } else {
            print('<a href="index.php" class="back_home small">ホーム画面に戻る</a>');
        } ?>

    </div>
</body>

</html>