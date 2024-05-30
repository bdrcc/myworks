<?php
session_start();


if (!isset($_GET['re'])) { // 1周目の画面訪問の場合

    if (!isset($_SESSION['a'])) { // 1問目の画面の場合
        $_SESSION['a'] = [];
        $_SESSION['look_over'] = [];
    } else { // 2問目以降
        if (isset($_POST['ans'])) {
            $_SESSION['a'][$_POST['id'] - 1] = $_POST['ans'];
        } else {
            $_SESSION['a'][$_POST['id'] - 1] = '未回答';
        }

        if (isset($_POST['look_over'])) {
            $_SESSION['look_over'][$_POST['id'] - 1] = 'on';
        } else {
            $_SESSION['look_over'][$_POST['id'] - 1] = 'off';
        }

        if (isset($_GET['back'])) {
            header('Location:end.php');
            exit();
        }
    }

    if (!isset($_SESSION['q'])) { //  セッションの中身がない、つまり初訪問の時

        setlocale(LC_ALL, 'ja_JP.UTF-8'); // サーバーで文字化けしないように書くもの
        $file = 'data.csv';
        $data = file_get_contents($file);
        $data = mb_convert_encoding($data, 'UTF-8', 'sjis-win');
        $temp = tmpfile(); // 一時的なコピーファイルを作成
        $csv = [];
        fwrite($temp, $data);
        rewind($temp);
        while (($data = fgetcsv($temp, 0, ",")) !== FALSE) {
            $csv[] = $data;
        }
        fclose($temp);
        shuffle($csv); // 配列をシャッフルする
        $_SESSION['q'] = $csv; // セッションに保存
    } else { // 再読み込みされた、つまり2回目以降の場合
        $csv = $_SESSION['q'];
    }

    if (!isset($_POST['id'])) { // 初回は1問目
        $id = 0;
    } else { // それ以降
        $id = $_POST['id'];
    }
} else { // 見直しで$_GET['re']が来ているとき
    // $_GET['id']を使用するだけ
    $csv = $_SESSION['q'];
    $id = $_GET['id'] - 1;
}

// 問題番号・リンク用に、変数を設定する
$next = $id + 1;

if ($id > 9) { // 10問目を終えると、自動で結果画面に移行する
    header('Location:end.php');
    exit();
}

// 問題の順番を入れ替える
$problem = [$csv[$id][1], $csv[$id][2], $csv[$id][3]];
// array_slice($csv[$id],1);でもよい？
shuffle($problem);
?>

<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>問題ページ / 10問クイズ</title>
    <meta name="description" content="3択問題が表示されるページです。「次へ」をクリックすると、新たな問題が表示されます。また、10問解き終えると、自分の解答一覧に移動します。">
    <link rel="stylesheet" href="style.css">
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
</head>

<body>
    <div class="main">
        <h1>問題<?php print($next); ?></h1>
        <h2><?php print($csv[$id][0]); ?></h2>

        <form action="<?php if (isset($_GET['re'])) {
                            print("quiz.php?back=end");
                        } ?>" method="post">
            <input type="hidden" name="id" value="<?php print($next); ?>">

            <label for="1">
                <p class="problem">
                    <input type="radio" id="1" name="ans" value="<?php print($problem[0]); ?>">
                    <?php print($problem[0]); ?>
                </p>
            </label>

            <label for="2">
                <p class="problem">
                    <input type="radio" id="2" name="ans" value="<?php print($problem[1]); ?>">
                    <?php print($problem[1]); ?>
                </p>
            </label>

            <label for="3">
                <p class="problem">
                    <input type="radio" id="3" name="ans" value="<?php print($problem[2]); ?>">
                    <?php print($problem[2]); ?>
                </p>
            </label>
            <label for="check">
                <p><input type="checkbox" name="look_over" id="check" <?php
                                                                        if (isset($_GET['re']) and $_SESSION['look_over'][$id] == 'on') {
                                                                            print('checked');
                                                                        }
                                                                        ?>>あとで見る</p>
            </label>

            <p class="submit"><input type="submit" value="<?php
                                                            if (isset($_GET['re'])) {
                                                                print('解答して一覧へ戻る');
                                                            } else {
                                                                print('次へ');
                                                            }
                                                            ?>"></p>

        </form>
    </div>
</body>

</html>