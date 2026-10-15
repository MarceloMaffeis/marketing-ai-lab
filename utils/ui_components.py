import streamlit as st

def render_anti_fraud_shield():
    """
    Injeta proteção contra incorporação indevida em iFrames (Clickjacking)
    e exibe aviso de proteção de uso educacional sob licença MIT.
    """
    st.markdown(
        """
        <script>
        try {
            if (window.self !== window.top) {
                // Tenta quebrar a moldura (breakout)
                window.top.location = window.self.location;
            }
        } catch (e) {
            console.warn("Executando dentro de container/iframe protegido.");
        }
        </script>
        """,
        unsafe_allow_html=True
    )

def render_top_nav(current_page: str = ""):
    """
    Renderiza um menu de navegação superior horizontal com botões diretos
    para alternar entre as ferramentas sem ocupar espaço na barra lateral.
    """
    render_anti_fraud_shield()

    with st.container():
        st.markdown(
            """
            <style>
            .nav-badge-open {
                display: inline-block;
                background-color: #0369a1;
                color: #e0f2fe;
                padding: 2px 8px;
                border-radius: 12px;
                font-size: 0.75rem;
                font-weight: 600;
                margin-bottom: 6px;
            }
            .nav-container {
                background: #1e293b;
                border: 1px solid #334155;
                border-radius: 8px;
                padding: 8px 12px;
                margin-bottom: 1rem;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        with st.expander("🧭 **Menu Rápido de Ferramentas (Trocar de Tela sem Barra Lateral)**", expanded=False):
            st.caption("Acesse qualquer um dos laboratórios práticos em 1 clique:")
            r1_c1, r1_c2, r1_c3, r1_c4, r1_c5 = st.columns(5)
            with r1_c1:
                if st.button("🏠 Início / Hub", key="topnav_home", use_container_width=True, disabled=(current_page == "home")):
                    st.switch_page("app.py")
            with r1_c2:
                if st.button("🔍 1. SEO & GEO", key="topnav_m1", use_container_width=True, disabled=(current_page == "m1")):
                    st.switch_page("pages/1_🔍_Auditoria_SEO_e_Palavras_Chave.py")
            with r1_c3:
                if st.button("🤖 2. Chatbot RAG", key="topnav_m2", use_container_width=True, disabled=(current_page == "m2")):
                    st.switch_page("pages/2_🤖_Chatbot_e_Atendimento.py")
            with r1_c4:
                if st.button("📈 3. Matriz KPIs", key="topnav_m3", use_container_width=True, disabled=(current_page == "m3")):
                    st.switch_page("pages/3_📈_Matriz_e_Calculadora_de_KPIs.py")
            with r1_c5:
                if st.button("🎯 4. Mídia RTB", key="topnav_m4", use_container_width=True, disabled=(current_page == "m4")):
                    st.switch_page("pages/4_🎯_Simulador_Programatica.py")

            r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
            with r2_c1:
                if st.button("🛍️ 5. Recomendação UX", key="topnav_m5", use_container_width=True, disabled=(current_page == "m5")):
                    st.switch_page("pages/5_🛍️_Recomendacao_e_UX.py")
            with r2_c2:
                if st.button("✍️ 6. Copywriting IA", key="topnav_m6", use_container_width=True, disabled=(current_page == "m6")):
                    st.switch_page("pages/6_✍️_Copy_e_Criacao_IA.py")
            with r2_c3:
                if st.button("📊 7. Dashboard BI", key="topnav_m7", use_container_width=True, disabled=(current_page == "m7")):
                    st.switch_page("pages/7_📊_Dashboard_KPIs_Preditivo.py")
            with r2_c4:
                if st.button("🌐 8. Hub de Ferramentas", key="topnav_m8", use_container_width=True, disabled=(current_page == "m8")):
                    st.switch_page("pages/8_🌐_Hub_de_Ferramentas_e_Buscas.py")

def render_sidebar_header():
    """Renderiza o cabeçalho padrão na barra lateral."""
    st.sidebar.markdown(
        """
        <div style="margin-bottom: 1rem;">
            <h2 style="margin: 0; font-size: 1.4rem; font-weight: 800; color: #f8fafc;">
                🚀 Marketing AI Lab
            </h2>
            <p style="margin: 0; font-size: 0.8rem; color: #38bdf8;">
                Open Educational Platform • Licença MIT
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_sidebar_footer():
    """Renderiza o rodapé institucional na barra lateral com licença MIT e aviso anti-fraude."""
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <div style="font-size: 0.78rem; color: #94a3b8; line-height: 1.5;">
            <p style="margin-bottom: 4px;">📜 <strong>Código Aberto sob Licença MIT</strong></p>
            <p style="margin-bottom: 8px;">Uso livre para estudo, cópias e projetos derivados.</p>
            <div style="background-color: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 4px; padding: 6px; font-size: 0.72rem; color: #fca5a5;">
                ⚠️ <strong>Aviso Anti-Fraude:</strong> Esta instância pública é 100% gratuita. É proibida a venda ou cobrança de acesso a esta URL.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_academic_footer():
    """Renderiza o rodapé acadêmico, licença MIT e aviso legal."""
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; margin-top: 2rem; margin-bottom: 1.5rem;">
            <p style="font-size: 0.95rem; font-weight: 600; color: #cbd5e1; margin-bottom: 4px;">
                🎓 Projeto Aberto de Educação em Marketing com Inteligência Artificial — Licença MIT
            </p>
            <p style="font-size: 0.85rem; color: #94a3b8; margin-top: 0; margin-bottom: 16px;">
                Disponível publicamente para estudo, modificações, forks e desenvolvimento livre de novos produtos.
            </p>
            <div style="background-color: rgba(245, 158, 11, 0.08); border-left: 4px solid #f59e0b; padding: 12px 18px; border-radius: 6px; text-align: left; max-width: 950px; margin: 0 auto;">
                <p style="font-size: 0.78rem; color: #fbbf24; margin: 0; line-height: 1.5;">
                    ⚠️ <strong>Aviso Legal & Diretrizes de Uso:</strong> Este software tem finalidade didática e acadêmica. As predições, cálculos de métricas de mídia, estimativas de leilão e diagnósticos gerados são simulações computacionais para aprendizado e não substituem plataformas oficiais de anúncios (Meta Ads, Google Ads), ferramentas homologadas de CRM ou a responsabilidade técnica de profissionais habilitados. É vedada a revenda desta URL pública de demonstração.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

