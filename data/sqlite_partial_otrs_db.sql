--
-- PostgreSQL database dump
--

CREATE TABLE article (
    id bigint NOT NULL,
    ticket_id bigint NOT NULL,
    article_type_id smallint NOT NULL,
    article_sender_type_id smallint NOT NULL,
    a_from character varying(3800),
    a_reply_to character varying(500),
    a_to character varying(3800),
    a_cc character varying(3800),
    a_subject character varying(3800),
    a_message_id character varying(3800),
    a_message_id_md5 character varying(32),
    a_in_reply_to character varying(3800),
    a_references character varying(3800),
    a_content_type character varying(250),
    a_body character varying NOT NULL,
    incoming_time integer NOT NULL,
    content_path character varying(250),
    valid_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);

--
-- Name: article_type; Type: TABLE; Schema: public; Owner: otrs; Tablespace: 
--

CREATE TABLE article_type (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    comments character varying(250),
    valid_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);

--
-- Name: customer_company; Type: TABLE; Schema: public; Owner: otrs; Tablespace: 
--

CREATE TABLE customer_company (
    customer_id character varying(150) NOT NULL,
    name character varying(200) NOT NULL,
    street character varying(200),
    zip character varying(200),
    city character varying(200),
    country character varying(200),
    url character varying(200),
    comments character varying(250),
    valid_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);


CREATE TABLE customer_user (
    id integer NOT NULL,
    login character varying(200) NOT NULL,
    email character varying(150) NOT NULL,
    customer_id character varying(150) NOT NULL,
    pw character varying(64),
    title character varying(50),
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    phone character varying(150),
    fax character varying(150),
    mobile character varying(150),
    street character varying(150),
    zip character varying(200),
    city character varying(200),
    country character varying(200),
    comments character varying(250),
    valid_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);


CREATE TABLE queue (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    group_id integer NOT NULL,
    unlock_timeout integer,
    first_response_time integer,
    first_response_notify smallint,
    update_time integer,
    update_notify smallint,
    solution_time integer,
    solution_notify smallint,
    system_address_id smallint NOT NULL,
    calendar_name character varying(100),
    default_sign_key character varying(100),
    salutation_id smallint NOT NULL,
    signature_id smallint NOT NULL,
    follow_up_id smallint NOT NULL,
    follow_up_lock smallint NOT NULL,
    comments character varying(250),
    valid_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);


--
-- Name: ticket; Type: TABLE; Schema: public; Owner: otrs; Tablespace: 
--

CREATE TABLE ticket (
    id bigint NOT NULL,
    tn character varying(50) NOT NULL,
    title character varying(255),
    queue_id integer NOT NULL,
    ticket_lock_id smallint NOT NULL,
    type_id smallint,
    service_id integer,
    sla_id integer,
    user_id integer NOT NULL,
    responsible_user_id integer NOT NULL,
    ticket_priority_id smallint NOT NULL,
    ticket_state_id smallint NOT NULL,
    customer_id character varying(150),
    customer_user_id character varying(250),
    timeout integer NOT NULL,
    until_time integer NOT NULL,
    escalation_time integer NOT NULL,
    escalation_update_time integer NOT NULL,
    escalation_response_time integer NOT NULL,
    escalation_solution_time integer NOT NULL,
    archive_flag smallint DEFAULT 0 NOT NULL,
    create_time_unix bigint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);


CREATE TABLE ticket_history (
    id bigint NOT NULL,
    name character varying(200) NOT NULL,
    history_type_id smallint NOT NULL,
    ticket_id bigint NOT NULL,
    article_id bigint,
    type_id smallint NOT NULL,
    queue_id integer NOT NULL,
    owner_id integer NOT NULL,
    priority_id smallint NOT NULL,
    state_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);


--
-- Name: ticket_priority; Type: TABLE; Schema: public; Owner: otrs; Tablespace: 
--

CREATE TABLE ticket_priority (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    valid_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);


--
-- Name: ticket_state; Type: TABLE; Schema: public; Owner: otrs; Tablespace: 
--

CREATE TABLE ticket_state (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    comments character varying(250),
    type_id smallint NOT NULL,
    valid_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);


--
-- Name: ticket_type; Type: TABLE; Schema: public; Owner: otrs; Tablespace: 
--

CREATE TABLE ticket_type (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    valid_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);


--
-- Name: ticket_type_id_seq; Type: SEQUENCE; Schema: public; Owner: otrs
--
CREATE TABLE time_accounting (
    id bigint NOT NULL,
    ticket_id bigint NOT NULL,
    article_id bigint,
    time_unit numeric(10,2) NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);

--
-- Name: users; Type: TABLE; Schema: public; Owner: otrs; Tablespace: 
--

CREATE TABLE users (
    id integer NOT NULL,
    login character varying(200) NOT NULL,
    pw character varying(64) NOT NULL,
    title character varying(50),
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    valid_id smallint NOT NULL,
    create_time timestamp(0) ,
    create_by integer NOT NULL,
    change_time timestamp(0) ,
    change_by integer NOT NULL
);

