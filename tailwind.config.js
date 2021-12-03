const colors = require('tailwindcss/colors')

module.exports = {
    purge: [],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            spacing: {
                '25vh': '25vh',
                '50vh': '50vh',
                '75vh': '75vh',
            },
        },
        colors: {
            teal: colors.teal,
            black: colors.black,
            white: colors.white,
            gray: colors.coolGray,
            red: colors.red,
            yellow: colors.amber,
            blue: colors.blue,
            green: colors.green,
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
