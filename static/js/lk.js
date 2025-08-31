Vue.createApp({
    components: {
        VForm: VeeValidate.Form,
        VField: VeeValidate.Field,
        ErrorMessage: VeeValidate.ErrorMessage,
    },
    data() {
        return {
            Edit: false,
            Name: '',
            Phone: '',
            Email: '',
            Address: '',
            Schema: {
            }
        }
    },
    mounted() {
        this.loadProfile();
    },
    methods: {
        loadProfile() {
            fetch('/api/profile/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                credentials: 'same-origin'
            })
            .then(response => response.json())
            .then(data => {
                this.Name = data.name || '';
                this.Phone = data.phonenumber || '';
                this.Email = data.email || '';
            })
            .catch(error => {
                console.error('Ошибка загрузки профиля:', error);
            });
        },

        ApplyChanges() {
            this.Edit = false;

            fetch('/api/profile/update/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                credentials: 'same-origin',
                body: JSON.stringify({
                    name: this.Name,
                    phonenumber: this.Phone,
                    email: this.Email
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    console.log('Профиль обновлен:', data.message);
                    alert('Профиль успешно обновлен!');
                }
            })
            .catch(error => {
                console.error('Ошибка обновления профиля:', error);
                alert('Ошибка при обновлении профиля');
            });
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
}).mount('#LK');