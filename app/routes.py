
from flask import Blueprint, render_template, request, redirect, url_for, send_file
from datetime import date
from .models import db, Quote
import io
from xhtml2pdf import pisa

main = Blueprint("main", __name__)

@main.route("/quotes")
def list_quotes():
    quotes = Quote.query.all()
    return render_template("quotes/list.html", quotes=quotes)

@main.route("/quotes/new", methods=["GET", "POST"])
def new_quote():
    if request.method == "POST":
        q = Quote(
            quote_no=request.form["quote_no"],
            client_name=request.form["client_name"],
            product_name=request.form["product_name"],
            unit_price=float(request.form["unit_price"]),
            quantity=int(request.form["quantity"]),
            total_price=round(float(request.form["unit_price"]) * int(request.form["quantity"]),2),
            quote_date=date.today().isoformat(),
            notes=request.form["notes"]
        )
        db.session.add(q)
        db.session.commit()
        return redirect(url_for("main.list_quotes"))
    return render_template("quotes/form.html", action='create')

@main.route("/quotes/edit/<int:qid>", methods=["GET","POST"])
def edit_quote(qid):
    q = Quote.query.get_or_404(qid)
    if request.method=="POST":
        q.quote_no=request.form["quote_no"]
        q.client_name=request.form["client_name"]
        q.product_name=request.form["product_name"]
        q.unit_price=float(request.form["unit_price"])
        q.quantity=int(request.form["quantity"])
        q.total_price=round(q.unit_price*q.quantity,2)
        q.notes=request.form["notes"]
        db.session.commit()
        return redirect(url_for("main.list_quotes"))
    return render_template("quotes/form.html", quote=q, action='edit')

@main.route("/quotes/delete/<int:qid>")
def delete_quote(qid):
    q = Quote.query.get_or_404(qid)
    db.session.delete(q)
    db.session.commit()
    return redirect(url_for("main.list_quotes"))

@main.route("/quotes/<int:qid>/pdf")
def quote_pdf(qid):
    q = Quote.query.get_or_404(qid)
    html = render_template("quotes/pdf.html", quote=q)
    pdf = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(html), dest=pdf)
    pdf.seek(0)
    return send_file(pdf, download_name=f"Quote_{q.quote_no}.pdf", as_attachment=True)

# 🔽 加上這段
@main.route("/")
def index():
    return redirect(url_for("main.list_quotes"))

