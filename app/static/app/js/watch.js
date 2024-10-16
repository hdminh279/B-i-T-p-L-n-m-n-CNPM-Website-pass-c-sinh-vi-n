// Lấy phần tử chat container và các nút
const chatContainer = document.getElementById('chat-container');
const chatButton = document.getElementById('chat-button');
const closeChatButton = document.getElementById('close-chat');

// Khi nhấn vào nút "Chat với người bán hàng", hiện hộp chat
chatButton.addEventListener('click', function() {
    chatContainer.classList.remove('hidden');
});

// Khi nhấn vào nút "✖", ẩn hộp chat
closeChatButton.addEventListener('click', function() {
    chatContainer.classList.add('hidden');
});
var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product  // Lấy product id từ data-product attribute
        var action = this.dataset.action      // Lấy action từ data-action attribute
        console.log('productId:', productId, 'action:', action)

        // Gọi hàm để cập nhật giỏ hàng, ví dụ bằng AJAX
        updateUserOrder(productId, action)
    })
}

function updateUserOrder(productId, action) {
    console.log('Gửi data...', productId, action)
    
    var url = '/update_item/'  // Đường dẫn tới view xử lý

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,  // Đảm bảo bạn có CSRF token ở đây
        },
        body: JSON.stringify({'productId': productId, 'action': action})  // Gửi productId và action qua AJAX
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()  // Tải lại trang sau khi cập nhật giỏ hàng
    })
}
