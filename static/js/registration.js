Vue.createApp({
    delimiters: ['[[', ']]'],
    components: {
        VForm: VeeValidate.Form,
        VField: VeeValidate.Field,
        ErrorMessage: VeeValidate.ErrorMessage,
    },
    data() {
        return {
            RegSchema: {
                reg: (value) => {
                    if (value) {
                        return true;
                    }
                    return 'Поле не заполнено';
                },
                phone_format: (value) => {
                    const regex = /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {
                        return '⚠ Формат телефона нарушен';
                    }
                    return true;
                },
                name_format: (value) => {
                    if (!value) {
                        return true;
                    }
                    if (value.length < 2) {
                        return '⚠ Имя должно содержать минимум 2 символа';
                    }
                    if (!/^[a-zA-Zа-яА-ЯёЁ\s\-]+$/.test(value)) {
                        return '⚠ Имя содержит недопустимые символы';
                    }
                    return true;
                }
            },
            Step: 'Number',
            RegInput: '',
            EnteredNumber: '',
            EnteredName: '',
            isLoading: false,
            errorMessage: ''
        }
    },
    methods: {
        async RegSubmit() {
            if (this.Step === 'Number') {
                const phoneValid = this.RegSchema.phone_format(this.RegInput);
                if (phoneValid !== true) {
                    return;
                }
                this.Step = 'Name'
                this.EnteredNumber = this.RegInput
                this.RegInput = ''
            }
            else if (this.Step === 'Name') {
                const nameValid = this.RegSchema.name_format(this.RegInput);
                if (nameValid !== true) {
                    return;
                }

                this.isLoading = true;
                this.errorMessage = '';

                try {
                    const response = await fetch('/api/register/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': this.getCookie('csrftoken')
                        },
                        body: JSON.stringify({
                            phonenumber: this.EnteredNumber,
                            name: this.RegInput
                        })
                    });

                    if (response.ok) {
                        const data = await response.json();
                        this.Step = 'Finish';
                        this.EnteredName = this.RegInput;
                        this.RegInput = 'Регистрация успешна!';
                    } else {
                        const errorData = await response.json();
                        this.errorMessage = errorData.phonenumber ?
                            'Этот номер телефона уже зарегистрирован' :
                            'Ошибка регистрации';
                    }
                } catch (error) {
                    this.errorMessage = 'Ошибка соединения с сервером';
                } finally {
                    this.isLoading = false;
                }
            }
        },
        Reset() {
            this.Step = 'Number';
            this.RegInput = '';
            this.EnteredNumber = '';
            this.EnteredName = '';
            this.errorMessage = '';
        },
        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    }
}).mount('#RegModal')