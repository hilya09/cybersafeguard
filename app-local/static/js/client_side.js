$(document).ready(function () {
  // -[Animasi Scroll]---------------------------

  $(".navbar a, .navbar-show-more a, footer a[href='#halamanku']").on("click", function (event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $("html, body").animate(
        {
          scrollTop: $(hash).offset().top,
        },
        900,
        function () {
          window.location.hash = hash;
        }
      );
    }
  });

  $(window).scroll(function () {
    $(".slideanim").each(function () {
      var pos = $(this).offset().top;
      var winTop = $(window).scrollTop();
      if (pos < winTop + 600) {
        $(this).addClass("slide");
      }
    });
  });

  // -[Prediksi Model untuk Phishing Detection]---------------
  $("#prediksi_submit").click(function (e) {
    e.preventDefault();

    // Set data link url dari pengguna
    var input_link = $("#inputVal_link").val();
    // Panggil API dengan timeout 1 detik (1000 ms)
    setTimeout(function () {
      try {
        $.ajax({
          url: "/api/deteksi",
          type: "POST",
          data: { data: input_link },
          success: function (res) {
            // Ambil hasil prediksi link dari API
            res_data_prediksi = res["data"];

            // Tampilkan hasil prediksi ke halaman web
            generate_prediksi(res_data_prediksi);
          },
        });
      } catch (e) {
        // Jika gagal memanggil API, tampilkan error di console
        console.log("Gagal !");
        console.log(e);
      }
    }, 1000);
  });

  // Fungsi untuk menampilkan hasil prediksi model
  function generate_prediksi(data_prediksi) {
    var str = "";
    str += "<p>URL Status: </p>";
    str += "<p>" + data_prediksi + "</p>";
    $("#hasil_prediksi").html(str);
  }
});
