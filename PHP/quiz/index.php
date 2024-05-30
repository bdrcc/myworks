<?php
session_start();
session_destroy();
?>

<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ホーム画面 / 10問クイズ</title>
    <meta name="description" content="3択問題の始めのページです。「スタート」をクリックすると、問題に移動します。">
    <link rel="stylesheet" href="style.css">
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
</head>

<body>
    <div class="home main">
        <div>
            <h1>常識クイズ</h1>
            <h2>全部で10問</h2>
            <a href="quiz.php">スタート</a>
        </div>
    </div>
</body>

</html>