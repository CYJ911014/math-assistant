# math_app.py - 完整版數學助手（包含代數、幾何、三角函數）
import streamlit as st
import sympy as sp
import math
import pandas as pd
import numpy as np
from datetime import datetime

# ========== 網頁配置 ==========
st.set_page_config(
    page_title="中學數學解題助手",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== 自定義CSS美化 ==========
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem !important;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border-left: 5px solid #3B82F6;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        width: 100%;
    }
    .success-box {
        background: #D1FAE5;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #10B981;
    }
</style>
""", unsafe_allow_html=True)

# ========== 初始化Session State ==========
if 'history' not in st.session_state:
    st.session_state.history = []
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "代數"

# ========== 標題區 ==========
st.markdown('<h1 class="main-title">🎓 中學數學解題助手</h1>', unsafe_allow_html=True)
st.markdown("---")

# ========== 側邊欄 ==========
with st.sidebar:
    st.markdown("### 📚 功能選單")
    
    tab = st.radio(
        "選擇解題類別",
        ["代數", "幾何", "三角函數", "歷史記錄", "使用說明"],
        index=["代數", "幾何", "三角函數", "歷史記錄", "使用說明"].index(st.session_state.current_tab)
    )
    st.session_state.current_tab = tab
    
    st.markdown("---")
    st.markdown("### 📊 統計資訊")
    st.info(f"解題紀錄: {len(st.session_state.history)} 筆")
    
    if st.button("🗑️ 清除歷史", use_container_width=True):
        st.session_state.history = []
        st.rerun()
    
    st.markdown("---")
    st.caption("🎓 數學研究所專題")
    st.caption("版本: 3.0 (完整網頁版)")

# ========== 記錄歷史的輔助函數 ==========
def add_to_history(prob_type, problem, solution):
    record = {
        "類型": prob_type,
        "問題": problem,
        "解答": solution,
        "時間": datetime.now().strftime("%H:%M:%S")
    }
    st.session_state.history.append(record)

# ========== 代數功能區 ==========
if tab == "代數":
    st.markdown("## 🧮 代數運算")
    
    alg_tab1, alg_tab2, alg_tab3 = st.tabs(["📊 方程求解", "🔍 表達式運算", "🧩 方程組"])
    
    # 標籤1：方程求解
    with alg_tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("#### 一元二次方程")
            st.markdown("**格式: ax² + bx + c = 0**")
            
            a = st.number_input("係數 a", value=1.0, key="quad_a")
            b = st.number_input("係數 b", value=-5.0, key="quad_b")
            c = st.number_input("常數項 c", value=6.0, key="quad_c")
            
            if st.button("求解二次方程", key="btn_quad"):
                if a == 0:
                    st.error("係數 a 不能為 0！")
                else:
                    x = sp.symbols('x')
                    equation = a*x**2 + b*x + c
                    solutions = sp.solve(equation, x)
                    
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown(f"**解為:** {solutions}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # 顯示判別式
                    D = b**2 - 4*a*c
                    with st.expander("📝 查看詳細步驟"):
                        st.write(f"1. 計算判別式: D = b² - 4ac = {b}² - 4×{a}×{c} = {D}")
                        if D > 0:
                            st.write(f"2. D > 0，有兩個實根")
                            st.write(f"3. 求根公式: x = [-b ± √D] / (2a)")
                            st.write(f"   x₁ = [{-b} + √{D}] / (2×{a}) = {solutions[0]}")
                            st.write(f"   x₂ = [{-b} - √{D}] / (2×{a}) = {solutions[1]}")
                    
                    add_to_history("二次方程", f"{a}x²+{b}x+{c}=0", str(solutions))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("#### 一元一次方程")
            st.markdown("**格式: ax + b = 0**")
            
            a_lin = st.number_input("係數 a", value=2.0, key="lin_a")
            b_lin = st.number_input("常數項 b", value=-8.0, key="lin_b")
            
            if st.button("求解一次方程", key="btn_lin"):
                if a_lin == 0:
                    st.error("係數 a 不能為 0！")
                else:
                    solution = -b_lin / a_lin
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown(f"**解為:** x = {solution:.4f}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    add_to_history("一次方程", f"{a_lin}x+{b_lin}=0", f"x={solution:.4f}")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # 標籤2：表達式運算
    with alg_tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("#### 因式分解")
            st.caption("例: x**2 - 4, x**2 + 2x + 1")
            
            factor_expr = st.text_input("輸入表達式", value="x**2 - 4", key="factor_expr")
            
            if st.button("因式分解", key="btn_factor"):
                try:
                    factored = sp.factor(factor_expr)
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown(f"**結果:** {factor_expr} = {factored}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    add_to_history("因式分解", factor_expr, str(factored))
                except Exception as e:
                    st.error(f"錯誤: {e}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("#### 表達式展開")
            st.caption("例: (x+1)**2, (x+2)*(x-3)")
            
            expand_expr = st.text_input("輸入表達式", value="(x+1)**2", key="expand_expr")
            
            if st.button("展開表達式", key="btn_expand"):
                try:
                    expanded = sp.expand(expand_expr)
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown(f"**結果:** {expand_expr} = {expanded}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    add_to_history("表達式展開", expand_expr, str(expanded))
                except Exception as e:
                    st.error(f"錯誤: {e}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # 表達式化簡
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("#### 表達式化簡")
        st.caption("例: (x**2 - 1)/(x - 1), sin(x)**2 + cos(x)**2")
        
        simplify_expr = st.text_input("輸入複雜表達式", value="(x**2 - 1)/(x - 1)", key="simplify_expr")
        
        if st.button("化簡表達式", key="btn_simplify"):
            try:
                simplified = sp.simplify(simplify_expr)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**結果:** {simplify_expr} = {simplified}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                add_to_history("表達式化簡", simplify_expr, str(simplified))
            except Exception as e:
                st.error(f"錯誤: {e}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 標籤3：方程組
    with alg_tab3:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("#### 二元一次方程組")
        st.markdown("**格式:** a₁x + b₁y = c₁")
        st.markdown("　　　　a₂x + b₂y = c₂")
        
        st.markdown("##### 第一個方程")
        col1, col2, col3 = st.columns(3)
        with col1:
            a1 = st.number_input("a₁", value=2.0, key="sys_a1")
        with col2:
            b1 = st.number_input("b₁", value=3.0, key="sys_b1")
        with col3:
            c1 = st.number_input("c₁", value=8.0, key="sys_c1")
        
        st.markdown("##### 第二個方程")
        col4, col5, col6 = st.columns(3)
        with col4:
            a2 = st.number_input("a₂", value=1.0, key="sys_a2")
        with col5:
            b2 = st.number_input("b₂", value=-1.0, key="sys_b2")
        with col6:
            c2 = st.number_input("c₂", value=1.0, key="sys_c2")
        
        if st.button("解方程組", key="btn_system"):
            try:
                x, y = sp.symbols('x y')
                eq1 = sp.Eq(a1*x + b1*y, c1)
                eq2 = sp.Eq(a2*x + b2*y, c2)
                solution = sp.solve((eq1, eq2), (x, y))
                
                if solution:
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown("**方程組:**")
                    st.write(f"{a1}x + {b1}y = {c1}")
                    st.write(f"{a2}x + {b2}y = {c2}")
                    st.write(f"**解:** x = {solution[x]}, y = {solution[y]}")
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.warning("方程組無解或無限多解")
                
                add_to_history("二元方程組", f"({a1},{b1},{c1}),({a2},{b2},{c2})", str(solution))
            except Exception as e:
                st.error(f"錯誤: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

# ========== 幾何功能區 ==========
elif tab == "幾何":
    st.markdown("## 📐 幾何計算")
    
    geom_tab1, geom_tab2, geom_tab3 = st.tabs(["📏 面積計算", "🔺 三角形", "⚫ 圓形"])
    
    with geom_tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("#### 三角形面積")
            st.markdown("**公式:** 面積 = ½ × 底 × 高")
            
            base = st.number_input("底邊長", value=10.0, min_value=0.0, key="tri_base")
            height = st.number_input("高", value=5.0, min_value=0.0, key="tri_height")
            
            if st.button("計算三角形面積", key="btn_tri_area"):
                area = 0.5 * base * height
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**面積** = ½ × {base} × {height}")
                st.markdown(f"**結果** = {area}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                add_to_history("三角形面積", f"底={base},高={height}", f"{area}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("#### 長方形面積")
            st.markdown("**公式:** 面積 = 長 × 寬")
            
            length = st.number_input("長", value=8.0, min_value=0.0, key="rect_len")
            width = st.number_input("寬", value=6.0, min_value=0.0, key="rect_width")
            
            if st.button("計算長方形面積", key="btn_rect_area"):
                area = length * width
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**面積** = {length} × {width}")
                st.markdown(f"**結果** = {area}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                add_to_history("長方形面積", f"長={length},寬={width}", f"{area}")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with geom_tab2:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("#### 畢氏定理")
        st.markdown("**公式:** a² + b² = c²")
        st.markdown("已知任意兩邊求第三邊")
        
        option = st.selectbox("已知條件", 
                             ["已知兩直角邊(a,b)求斜邊(c)",
                              "已知直角邊(a)和斜邊(c)求另一邊(b)",
                              "已知直角邊(b)和斜邊(c)求另一邊(a)"])
        
        if "兩直角邊" in option:
            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("直角邊 a", value=3.0, min_value=0.0, key="pyth_a")
            with col2:
                b = st.number_input("直角邊 b", value=4.0, min_value=0.0, key="pyth_b")
            
            if st.button("計算斜邊", key="btn_pyth_c"):
                c = math.sqrt(a**2 + b**2)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**斜邊 c** = √({a}² + {b}²)")
                st.markdown(f"**結果** = {c:.4f}")
                st.markdown('</div>', unsafe_allow_html=True)
                add_to_history("畢氏定理", f"a={a},b={b}", f"c={c:.4f}")
        
        elif "直角邊(a)和斜邊" in option:
            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("直角邊 a", value=3.0, min_value=0.0, key="pyth_a2")
            with col2:
                c = st.number_input("斜邊 c", value=5.0, min_value=0.0, key="pyth_c2")
            
            if st.button("計算另一邊", key="btn_pyth_b2"):
                if c <= a:
                    st.error("斜邊必須大於直角邊！")
                else:
                    b = math.sqrt(c**2 - a**2)
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown(f"**直角邊 b** = √({c}² - {a}²)")
                    st.markdown(f"**結果** = {b:.4f}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    add_to_history("畢氏定理", f"a={a},c={c}", f"b={b:.4f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with geom_tab3:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("#### 圓計算")
        st.markdown("**公式:** 面積 = π × r², 周長 = 2π × r")
        
        radius = st.number_input("半徑 r", value=5.0, min_value=0.0, key="circle_radius")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("計算圓面積", key="btn_circle_area"):
                area = math.pi * radius ** 2
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**面積** = π × {radius}²")
                st.markdown(f"**結果** = {area:.4f}")
                st.markdown('</div>', unsafe_allow_html=True)
                add_to_history("圓面積", f"半徑={radius}", f"{area:.4f}")
        
        with col2:
            if st.button("計算圓周長", key="btn_circle_circ"):
                circumference = 2 * math.pi * radius
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**周長** = 2π × {radius}")
                st.markdown(f"**結果** = {circumference:.4f}")
                st.markdown('</div>', unsafe_allow_html=True)
                add_to_history("圓周長", f"半徑={radius}", f"{circumference:.4f}")
        st.markdown('</div>', unsafe_allow_html=True)

# ========== 三角函數功能區 ==========
elif tab == "三角函數":
    st.markdown("## 📐 三角函數")
    
    trig_tab1, trig_tab2, trig_tab3 = st.tabs(["🔄 角度轉換", "📊 函數計算", "🔺 解直角三角形"])
    
    with trig_tab1:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("#### 角度單位轉換")
        
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("數值", value=180.0, key="angle_value")
            from_unit = st.selectbox("從單位", ["度(°)", "弧度(rad)"], key="angle_from")
        
        with col2:
            if st.button("執行轉換", key="btn_convert_angle"):
                if "度" in from_unit:
                    radians = math.radians(value)
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown(f"**{value}°** = {radians:.6f} 弧度")
                    st.markdown('</div>', unsafe_allow_html=True)
                    add_to_history("角度轉換", f"{value}°", f"{radians:.6f}弧度")
                else:
                    degrees = math.degrees(value)
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown(f"**{value} 弧度** = {degrees:.6f}°")
                    st.markdown('</div>', unsafe_allow_html=True)
                    add_to_history("角度轉換", f"{value}弧度", f"{degrees:.6f}°")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with trig_tab2:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("#### 三角函數值")
        
        col1, col2 = st.columns(2)
        with col1:
            angle = st.number_input("角度值", value=45.0, key="trig_angle")
            unit = st.selectbox("單位", ["度(°)", "弧度(rad)"], key="trig_unit")
        
        with col2:
            if st.button("計算函數值", key="btn_trig_values"):
                if "度" in unit:
                    angle_rad = math.radians(angle)
                    angle_str = f"{angle}°"
                else:
                    angle_rad = angle
                    angle_str = f"{angle}弧度"
                
                sin_val = math.sin(angle_rad)
                cos_val = math.cos(angle_rad)
                tan_val = math.tan(angle_rad) if abs(angle_rad % math.pi - math.pi/2) > 0.001 else "未定義"
                
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**角度:** {angle_str}")
                st.markdown(f"**sin** = {sin_val:.6f}")
                st.markdown(f"**cos** = {cos_val:.6f}")
                st.markdown(f"**tan** = {tan_val if isinstance(tan_val, str) else f'{tan_val:.6f}'}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                add_to_history("三角函數", f"{angle_str}", f"sin={sin_val:.4f},cos={cos_val:.4f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with trig_tab3:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("#### 解直角三角形")
        st.markdown("已知兩邊求第三邊和角度")
        
        known_option = st.selectbox("已知條件",
                                   ["已知兩直角邊(a,b)",
                                    "已知直角邊(a)和斜邊(c)",
                                    "已知直角邊(b)和斜邊(c)"])
        
        if "兩直角邊" in known_option:
            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("直角邊 a", value=3.0, min_value=0.0, key="rt_a")
            with col2:
                b = st.number_input("直角邊 b", value=4.0, min_value=0.0, key="rt_b")
            
            if st.button("解三角形", key="btn_solve_rt1"):
                c = math.sqrt(a**2 + b**2)
                angle_A = math.degrees(math.atan(a/b))
                angle_B = 90 - angle_A
                
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown("**結果:**")
                st.markdown(f"斜邊 c = √({a}² + {b}²) = {c:.4f}")
                st.markdown(f"角 A = arctan({a}/{b}) = {angle_A:.2f}°")
                st.markdown(f"角 B = 90° - {angle_A:.2f}° = {angle_B:.2f}°")
                st.markdown('</div>', unsafe_allow_html=True)
                
                add_to_history("解直角三角形", f"a={a},b={b}", f"c={c:.2f},A={angle_A:.1f}°,B={angle_B:.1f}°")
        
        elif "直角邊(a)和斜邊" in known_option:
            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("直角邊 a", value=3.0, min_value=0.0, key="rt_a2")
            with col2:
                c = st.number_input("斜邊 c", value=5.0, min_value=0.0, key="rt_c2")
            
            if st.button("解三角形", key="btn_solve_rt2"):
                if c <= a:
                    st.error("斜邊必須大於直角邊！")
                else:
                    b = math.sqrt(c**2 - a**2)
                    angle_A = math.degrees(math.asin(a/c))
                    angle_B = 90 - angle_A
                    
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown("**結果:**")
                    st.markdown(f"直角邊 b = √({c}² - {a}²) = {b:.4f}")
                    st.markdown(f"角 A = arcsin({a}/{c}) = {angle_A:.2f}°")
                    st.markdown(f"角 B = 90° - {angle_A:.2f}° = {angle_B:.2f}°")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    add_to_history("解直角三角形", f"a={a},c={c}", f"b={b:.2f},A={angle_A:.1f}°,B={angle_B:.1f}°")
        st.markdown('</div>', unsafe_allow_html=True)

# ========== 歷史記錄區 ==========
elif tab == "歷史記錄":
    st.markdown("## 📜 解題歷史記錄")
    
    if not st.session_state.history:
        st.info("還沒有解題記錄，快去解題吧！")
    else:
        # 顯示為表格
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # 統計資訊
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("總記錄數", len(df))
        with col2:
            st.metric("代數問題", len(df[df["類型"].str.contains("方程|因式|表達式")]))
        with col3:
            st.metric("幾何問題", len(df[df["類型"].str.contains("面積|圓|畢氏")]))
        
        # 下載按鈕
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 下載CSV檔案",
            data=csv,
            file_name=f"math_history_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        # 清除按鈕
        if st.button("🗑️ 清除所有記錄", use_container_width=True, type="secondary"):
            st.session_state.history = []
            st.rerun()

# ========== 使用說明區 ==========
elif tab == "使用說明":
    st.markdown("## 📖 使用說明")
    
    with st.expander("🎯 快速入門", expanded=True):
        st.markdown("""
        1. **選擇功能類別**：在左側選單選擇代數、幾何或三角函數
        2. **輸入數值**：在對應的輸入框中輸入數字或表達式
        3. **點擊計算**：按下計算按鈕查看結果
        4. **查看歷史**：所有計算會自動保存到歷史記錄
        """)
    
    with st.expander("🧮 代數功能"):
        st.markdown("""
        ### 一元二次方程
        - 格式: `ax² + bx + c = 0`
        - 輸入三個係數即可求解
        - 提供判別式分析和詳細步驟
        
        ### 一元一次方程
        - 格式: `ax + b = 0`
        - 當 a ≠ 0 時，解為 `x = -b/a`
        
        ### 因式分解
        - 支援多項式因式分解
        - 例: `x**2 - 4` → `(x-2)*(x+2)`
        
        ### 表達式展開
        - 展開多項式乘積
        - 例: `(x+1)**2` → `x**2 + 2x + 1`
        
        ### 二元一次方程組
        - 格式: `a₁x + b₁y = c₁`, `a₂x + b₂y = c₂`
        - 輸入六個係數求解
        """)
    
    with st.expander("📐 幾何功能"):
        st.markdown("""
        ### 面積計算
        - 三角形面積: `½ × 底 × 高`
        - 長方形面積: `長 × 寬`
        
        ### 畢氏定理
        - 公式: `a² + b² = c²`
        - 已知任意兩邊求第三邊
        
        ### 圓計算
        - 面積: `π × r²`
        - 周長: `2π × r`
        """)
    
    with st.expander("📐 三角函數"):
        st.markdown("""
        ### 角度轉換
        - 度(°) ↔ 弧度(rad) 互換
        
        ### 函數計算
        - 計算 sin, cos, tan 值
        - 支援度和弧度單位
        
        ### 解直角三角形
        - 已知兩邊求第三邊和角度
        - 自動計算所有未知量
        """)
    
    st.markdown("---")
    st.markdown("**💡 提示:** 所有計算結果會自動保存，可在「歷史記錄」中查看和下載")

# ========== 頁腳 ==========
st.markdown("---")
st.caption("🎓 數學研究所專題 | 中學數學解題助手 | 網頁版 v3.0")

# ========== 自動重啟提示 ==========
if st.sidebar.checkbox("開啟自動重啟", value=False):
    st.sidebar.warning("開發模式：程式碼修改後會自動重啟")