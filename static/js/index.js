Vue.createApp({
    delimiters: ['[[', ']]'],
    name: "App",
    components: {
        VForm: VeeValidate.Form,
        VField: VeeValidate.Field,
        ErrorMessage: VeeValidate.ErrorMessage,
    },
    data() {
        return {
            schema1: {
                lvls: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' количество уровней';
                },
                form: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' форму торта';
                },
                topping: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' топпинг';
                }
            },
            schema2: {
                name: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' имя';
                },
                phone: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' телефон';
                },
                name_format: (value) => {
                    const regex = /^[a-zA-Zа-яА-Я]+$/
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат имени нарушен';
                    }
                    return true;
                },
                email_format: (value) => {
                    const regex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат почты нарушен';
                    }
                    return true;
                },
                phone_format:(value) => {
                    const regex = /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат телефона нарушен';
                    }
                    return true;
                },
                email: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' почту';
                },
                address: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' адрес';
                },
                date: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' дату доставки';
                },
                time: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' время доставки';
                } 
            },
            DATA: {
                Levels: window.INITIAL_DATA.levels,
                Forms: window.INITIAL_DATA.forms,
                Toppings: window.INITIAL_DATA.toppings,
                Berries: window.INITIAL_DATA.berries,
                Decors: window.INITIAL_DATA.decors
            },
            Costs: {
                Levels: window.INITIAL_DATA.levels_price,
                Forms: window.INITIAL_DATA.forms_price,
                Toppings: window.INITIAL_DATA.toppings_price,
                Berries: window.INITIAL_DATA.berries_price,
                Decors: window.INITIAL_DATA.decors_price,
                Words: window.INITIAL_DATA.curent_phrase_price
            },
            Levels: 0,
            Form: 0,
            Topping: 0,
            Berries: 0,
            Decor: 0,
            Words: '',
            Comments: '',
            Designed: false,

            Name: '',
            Phone: null,
            Email: null,
            Address: null,
            Dates: null,
            Time: null,
            DelivComments: ''
        }
    },
    methods: {
        ToStep4() {
            this.Designed = true
            setTimeout(() => this.$refs.ToStep4.click(), 0);
        },
        Order(){
            fetch('/save_order/', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    level: this.DATA.Levels[this.Levels],
                    form: this.DATA.Forms[this.Form],
                    topping: this.DATA.Toppings[this.Topping],
                    berries: this.DATA.Berries[this.Berries],
                    decor: this.DATA.Decors[this.Decor],
                    phrase_on_cake: this.Words,
                    comment: this.Comments,
                    Name: this.Name,
                    Phone: this.Phone,
                    Email: this.Email,
                    Address: this.Address,
                    date: this.Dates,
                    time: this.Time,
                    courier_comment: this.DelivComments,
                    price: this.Cost
                })
            })
            console.log(this.DATA.Levels[this.Levels], this.DATA.Forms[this.Form], this.DATA.Toppings[this.Topping], 
                this.DATA.Berries[this.Berries], this.DATA.Decors[this.Decor], this.Words, this.Comments,
                this.Name, this.Phone, this.Email, this.Address, this.Dates, this.Time, this.DelivComments, this.Cost)
        }
    },
    computed: {
        Cost() {
            const curr_date = new Date()
            const combinedDateString = `${this.Dates}T${this.Time}`;
            const date = new Date(combinedDateString);
            const differenceInMilliseconds = date - curr_date;
            const hoursDifference = differenceInMilliseconds / (1000 * 60 * 60); 
            let K = hoursDifference <= 24 ? 1.2 : 1
            let W = this.Words ? this.Costs.Words : 0
            return (this.Costs.Levels[this.Levels] + this.Costs.Forms[this.Form] +
                this.Costs.Toppings[this.Topping] + this.Costs.Berries[this.Berries] +
                this.Costs.Decors[this.Decor] + W) * K
        }
    }
}).mount('#VueApp')