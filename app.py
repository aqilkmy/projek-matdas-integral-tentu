from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def integral_tentu():
    soal = None
    format_hasil = None
    input_fungsi = None
    a = None
    b = None

    if request.method == 'POST':
        try:
            # Def fungsi yg akan diintegral
            def fungsi(x, input_fungsi):
                return eval(input_fungsi)

            # Algoritma metode trapesium
            def integral_trapesium(a, b, n, input_fungsi):
                h = (b - a) / n
                sum =  (fungsi(a, input_fungsi) + fungsi(b, input_fungsi)) / 2

                for i in range(1, n):
                    sum += fungsi(a + i * h, input_fungsi)
                return sum * h

            # Input 
            input_fungsi = request.form['func']
            a = int(request.form['bts-bwh'])
            b = int(request.form['bts-ats'])
            n = 100

            # Hitung integral
            hasil = integral_trapesium(a, b, n, input_fungsi)

            # Format tampilan soal & hasil
            func_expr = sp.sympify(input_fungsi)
            soal = sp.latex(func_expr)  # Mengubah ke format LaTeX
            format_hasil =  f"{hasil:.1f}"
        except (KeyError, sp.SympifyError):
            hasil = "Masukkan Fungsi"

    # Return fungsi agar dpt ditampilkan di html
    return render_template('integral-tentu.html', input_fungsi=input_fungsi, a=a, b=b, format_hasil=format_hasil, soal=soal)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
