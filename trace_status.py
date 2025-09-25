import streamlit as st
from ontap_trace import stop_packet_trace, get_trace_status

st.title("Packet Trace Status")

trace_id = st.session_state.get('task_id')
if not trace_id:
    st.warning("No trace running currently.")
else:
    status = get_trace_status(trace_id)
    st.info(f"Trace Status: {status}")
    if st.button("Stop Trace"):
        stop_packet_trace(trace_id)
        st.success("Trace stopped successfully! 🛑")
