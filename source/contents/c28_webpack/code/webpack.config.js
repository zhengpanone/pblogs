// 通过Node模块操作，向外暴露一个配置对象
const path = require('path')

// 只要是插件，都要放到plugins节点中
// 根据指定页面 自动在内存中 生成一个页面
// 自动把打包好的bundle.js追加到页面中去
const htmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
    // 入口，表示要使用webpack打包那个文件
    entry: path.join(__dirname, './src/main.js'),

    output: {//输出文件相关配置
        //打包好的文件，输出到那个目录
        path: path.join(__dirname, './dist'),
        filename: 'bundle.js'//指定输出文件的名称
    },
    mode: 'development',
    plugins: [
        //创建一个在内存中生成htm页面的插件
        new htmlWebpackPlugin({
            template: path.join(__dirname, './src/index.html'),
            //指定模板页面，将来会根据指定的页面路径去生成内存中的页面
            filename: 'index.html'//指定生成页面的名称
        })
    ],
    module: {// 用于配置，所有的第三方模块加载器
        rules: [// 所有第三方模块的规则
            { test: /\.css$/, use: ['style-loader', 'css-loader'] },
            //配置处理.css文件的第三方loader的规则
            // 注意：webpack处理第三方文件的类型

            /*
             1、发现这个要处理的文件不是js文件，然后就去配置文件中，查找有没有对应的第三方loader规则
            2、如果能找到对应规则，就会调用对应的loader处理这种文件类型
            3、在调用loader的时候，是从后往前调用
            4、当最后一个loader调用完毕，会把处理的结果直接交给webpack进行打包合并，最终输出到bundle.js中 */
            //配置处理less文件的第三方loader规则
            { test: /\.less$/, use: ['style-loader', 'css-loader', 'less-loader'] },
            //  { test: /\.sass$/, use: ['style-loader', 'css-loader', 'sass-loader'] },
            //配置处理scss文件的第三方loader规则
            { test: /\.(png|jpg|gif|bmp|jpeg)$/, use: 'url-loader?limit=50020&name=[hash:8]-[name].[ext]' },
            //limit 给定的值是图片大小，单位byte ，如果引用图片大于或等于给定的值则不会被转为base64
            // name后面表示名称不修改，后缀名不修改
            { test: /\.(ttf|eot|svg|woff|woff2)$/, use: 'url-loader' },
            //配置Babel来转换高级Es语法
            { test: /\.js$/, use: 'babel-loader', exclude: /node_modules/ }, 
        ]

    }
}


