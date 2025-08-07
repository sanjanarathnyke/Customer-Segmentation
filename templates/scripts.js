        tailwind.config = {
            theme: {
                extend: {
                    animation: {
                        'gradient': 'gradient 8s ease infinite',
                        'float': 'float 6s ease-in-out infinite',
                        'pulse-glow': 'pulse-glow 2s ease-in-out infinite alternate',
                    },
                    keyframes: {
                        gradient: {
                            '0%, 100%': {
                                'background-size': '200% 200%',
                                'background-position': 'left center'
                            },
                            '50%': {
                                'background-size': '200% 200%',
                                'background-position': 'right center'
                            },
                        },
                        float: {
                            '0%, 100%': { transform: 'translateY(0px)' },
                            '50%': { transform: 'translateY(-10px)' },
                        },
                        'pulse-glow': {
                            '0%': { 'box-shadow': '0 0 20px rgba(79, 172, 254, 0.5)' },
                            '100%': { 'box-shadow': '0 0 30px rgba(79, 172, 254, 0.8)' },
                        }
                    }
                }
            }
        }