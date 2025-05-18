from app import create_app, db
from app.models.item import Category, Package, Color
from app.models.order import Factory

def seed():
    app = create_app()
    with app.app_context():
        db.create_all()
        cats = [("Trash can","A"),("Goldrose","B"),("Tray table (Funrniture)","C"),
                ("Shelving, Rack","D"),("Sport","E"),("Dry bag","F"),("Umbrella","G"),("Waterproof socks","H")]
        packs=[("彩盒","B"),("對折吊卡","C"),("白盒","V"),("綁卡","D"),("瓦楞盒","U"),("塑膠膜收縮包裝","K"),
               ("窗盒","W"),("彩套(含收縮膜)","S"),("展示盒","M"),("展售盒","Z"),("雙泡殼","J"),("工具袋","P"),
               ("PE袋","E"),("PVC袋","E"),("白盒貼標","L"),("棕盒貼標","R")]
        cols=[("Chrome","CH"),("Silver","S"),("Black","B")]
        facs=[("金星","A"),("江門外貿","B"),("SOL","A"),("承麟","B"),("麥箖","A")]
        for n,c in cats:
            if not Category.query.filter_by(code=c).first(): db.session.add(Category(name=n,code=c))
        for n,c in packs:
            if not Package.query.filter_by(name=n).first(): db.session.add(Package(name=n,code=c))
        for n,c in cols:
            if not Color.query.filter_by(code=c).first(): db.session.add(Color(name=n,code=c))
        for n,c in facs:
            if not Factory.query.filter_by(code=c).first(): db.session.add(Factory(name=n,code=c))
        db.session.commit()
        print("Seed done")
if __name__ == "__main__":
    seed()
