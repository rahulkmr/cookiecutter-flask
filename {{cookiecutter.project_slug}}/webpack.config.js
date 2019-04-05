const webpack = require('webpack');
const path = require('path');
const MiniCSSExtractPlugin = require('mini-css-extract-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')
const WebpackAssetsManifest = require('webpack-manifest-plugin');


const assetsPath = path.join(__dirname, '{{cookiecutter.project_slug}}', 'assets')

module.exports = {
    entry: {
        app_scripts: './{{cookiecutter.project_slug}}/assets/app.js',
        app_styles: './{{cookiecutter.project_slug}}/assets/app.scss',
        app_images: './{{cookiecutter.project_slug}}/assets/images.js'
    },
    output: {
        path: path.join(__dirname, '{{cookiecutter.project_slug}}', 'static', 'build'),
        publicPath: `/static/build/`,
        filename: '[name].[hash].js',
        chunkFilename: '[name]_[id].[chunkhash].js'
    },

    plugins: [
        new MiniCSSExtractPlugin({
            filename: '[name].[hash].css',
            chunkFilename: '[name]_[id].[chunkhash].css'
        }),
        new CleanWebpackPlugin(),
        new WebpackAssetsManifest(),
    ],
    module: {
        rules: [{
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: [{
                        loader: 'babel-loader',
                        options: {
                            plugins: ['syntax-dynamic-import'],
                            presets: [
                                [
                                    '@babel/preset-env',
                                    {
                                        modules: false
                                    }
                                ]
                            ]
                        },
                    },
                    'eslint-loader',
                ],
            },
            {
                test: /\.(scss|css)$/,
                use: [{
                        loader: MiniCSSExtractPlugin.loader
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            },
            {
                test: /\.(png|svg|jpg|gif)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            context: assetsPath,
                            name: '[path][name].[hash].[ext]',
                        }
                    },
                ]
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            context: assetsPath,
                            name: '[path][name].[hash].[ext]',
                        }
                    },
                ]
            }

        ]
    },
};
