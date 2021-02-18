<!--
  LZU COVID Health Report Dispatch Manually Front-end

  Copyright © 2021 Hollow Man(@HollowMan6). All rights reserved.

  This document is free software; you can redistribute it and/or modify it under the terms of the GNU General
  Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option)
  any later version.
-->

<!DOCTYPE html>
<html lang="zh-cn">

<head>
    <meta charset="UTF-8">
    <meta charset="UTF-8" name="viewport" content="width=device-width,initial-scale=0.6,maximum-scale=1.5,minimum-scale=0.6,user-scalable=yes">
    <meta name="keywords" content="兰州大学, 兰大, 疫情, 健康打卡, 自动" />
    <meta name="description" content="兰州大学疫情健康打卡手动触发前端。LZU COVID Health Report Dispatch Manually Front-end." />
    <meta name="robots" content="all" />
    <meta name="renderer" content="webkit" />
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
    <meta name="Author" content="Hollow Man" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css/out/water.css">
    <link rel="icon" href="https://avatars.githubusercontent.com/oa/1472343?s=64&v=4" type="image/png">
    <title>兰州大学疫情健康打卡手动触发</title>
    <script>
        <?php
        $refreshing = false;
        if (isset($_GET['refresh'])) {
            if (is_numeric($_GET['refresh']) && $_GET['refresh'] > 0) {
                $refreshing = true;
                echo "window.setTimeout(function(){ window.location.reload(); }," . strval($_GET['refresh'] * 1000) . ")";
            } else {
                echo "alert('URL中refresh参数不是正数!')";
            }
        }
        if (isset($_GET['report'])) {
            exec("cd ./../ && python job.py > /dev/null &");
            echo "alert('已手动触发打卡一次, 可能最多需要等待5分钟才会显示在日志中!');";
            echo "window.location = window.location.protocol + '//' + window.location.hostname + window.location.pathname";
            if ($refreshing) {
                echo "+ 'refresh=" . $_GET['refresh'] . "';";
            }
        }
        ?>
    </script>
</head>

<body>
    <h1 align="center">兰州大学疫情健康打卡手动触发</h1>
    <h3 align="center">LZU COVID Health Report Dispatch Manually</h3>
    <p align="center">
        <button onclick="window.location = window.location.protocol + '//' + window.location.hostname + window.location.pathname + '?report=1'">手动打卡一次</button>
        <button onclick="window.location.reload();">刷新</button>
    </p>
    <h2>手动打卡日志记录</h2>
    <pre><code>
    <?php
    if (is_file(__DIR__ . '/../vendor/autoload.php')) {
        require_once __DIR__ . '/../vendor/autoload.php';
    }
    $file_path = './../logs.txt';
    if (file_exists($file_path)) {
        $fp = fopen($file_path, "r");
        $str = fread($fp, filesize($file_path));
        $result = Parsedown::instance()->parse($str);
        echo $result;
    }
    ?>
</code></pre>
    <form action="./">
        <h3>设定自动刷新秒数(单位:秒)</h3>
        <input type="number" name="refresh" min="0" value="<?php if ($refreshing) echo $_GET['refresh'];
                                                            else echo 2; ?>">
        <input type="submit" value="确定">
    </form>
    <footer>
        <p align="center">
            <img src="https://hollowman.ml/img/logo.gif" width="30%" onclick="window.open('https://hollowman.ml','_blank')">
        </p>
        <h5 align="center">Copyright &copy; 2018-2021 <img width="20px" src="https://hollowman.ml/favicon.ico"> Hollow
            Man (<a href="https://github.com/HollowMan6" target="_blank">@HollowMan6</a>). All rights reserved.</h5>
        <p align="center">
            <img src="https://img.shields.io/badge/license-GPL-green" onclick="window.open('https://opensource.org/licenses/GPL-3.0/','_blank')">
            <img src="https://img.shields.io/badge/-%E2%9D%A4%20Open%20Source%20%E6%8D%90%E5%8A%A9%E6%88%91-Green?style=flat-square&logo=Github&logoColor=white&link=https://hollowman.ml/fund.html" onclick="window.open('https://hollowman.ml/fund.html','_blank')">
            <img src="https://img.shields.io/github/repo-size/HollowMan6/LZU-Auto-COVID-Health-Report.svg" onclick="window.open('https://github.com/HollowMan6/LZU-Auto-COVID-Health-Report','_blank')">
        </p>
    </footer>
</body>

</html>