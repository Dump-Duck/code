document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    let successMessage = document.querySelector('#success-message');
    let inputs = document.querySelectorAll('.input_footer');

   // Hiển thị thông báo lỗi đầu vào
    function showError(input, message) {
        const formControl = input.parentElement;
        formControl.className = 'form-control error';
        const small = formControl.querySelector('small');
        small.innerText = message;
    }

    /// Hiển thị  thành công
    function showSuccess(input) {
        const formControl = input.parentElement;
        formControl.className = 'form-control success';
        const small = formControl.querySelector('small');
        small.innerText = '';
    }

    // Lấy tên trường
    function getFieldName(input) {
        return input.id.charAt(0).toUpperCase() + input.id.slice(1);
    }

    /// Kiểm tra các trường bắt buộc
    function checkRequired(inputArr) {
        let isRequired = false;
        inputArr.forEach(function (input) {
            if (input.value.trim() === '') {
                showError(input, `${getFieldName(input)} is required`);
                isRequired = true;
            } else {
                showSuccess(input);
            }
        });
        return !isRequired;
    }

    /// Kiểm tra độ dài đầu vào
    function checkLength(input, min, max) {
        if (typeof input.value !== 'string') { // kiểm tra xem giá trị đầu vào có phải là chuỗi hay không
            return false;
        }
        if (input.value.trim().length < min) {
            showError(
                input,
                `${getFieldName(input)} must be at least ${min} characters`
            );
            return false;
        } else if (input.value.trim().length > max) {
            showError(
                input,
                `${getFieldName(input)} must be less than ${max} characters`
            );
            return false;
        } else {
            showSuccess(input);
            return true;
        }
    }

    // Check email is valid
    function checkEmail(input) {
        const emailRegex = /^\S+@\S+\.\S+$/;
        if (!emailRegex.test(input.value)) {
            showError(input, 'Email is not valid');
            return false;
        } else {
            showSuccess(input);
            return true;
        }
    }

    // Submit form
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        let isFormValid = true;

        if (!checkRequired([username, email])) {
            isFormValid = false;
        }

        if (!checkLength(username, 3, 15)) {
            isFormValid = false;
        }

        if (!checkEmail(email)) {
            isFormValid = false;
        }

        if (isFormValid) {
            form.reset();
            successMessage.style.display = 'block';
            setTimeout(() => {
                successMessage.style.display = 'none';
                console.log('Success message hidden');
            }, 3000);
        }
    });
});
