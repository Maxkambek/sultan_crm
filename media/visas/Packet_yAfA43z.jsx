import axios from "axios";
import { useEffect, useState } from "react";
import {} from "react";
import { Link } from "react-router-dom";
import { API_PATH, CONFIG } from "../constants/constants";

const Packet = () => {
  const [paketName, setPaketName] = useState();
  const [paketPrice, setPaketPrice] = useState();
  const [paketDateGo, setPaketDateGo] = useState();
  const [paketDateBack, setPaketDateBack] = useState();
  const [paketType, setPaketType] = useState();
  const [paketQuantity, setQuantity] = useState();
  const [paketReysInfo, setPaketReysInfo] = useState();
  const [paketAviaCompany, setPaketAviaCompany] = useState();
  const [paketMadinaHotel, setPaketMadinaHotel] = useState();
  const [paketMadinaDuration, setPaketMadinaDuration] = useState();
  const [paketMadinaDish, setPaketMadinaDish] = useState();
  const [paketMakkaHotel, setPaketMakkaHotel] = useState();
  const [paketMakkaDuration, setPaketMakkaDuration] = useState();
  const [paketMakkaDish, setPaketMakkaDish] = useState();
  const [paketDescription, setPaketDescription] = useState();
  const [paketDuration, setPaketDuration] = useState();

  const [paketUpdateName, setUpdatePaketName] = useState();
  const [paketUpdatePrice, setUpdatePaketPrice] = useState();
  const [paketUpdateDateGo, setUpdatePaketDateGo] = useState();
  const [paketUpdateDateBack, setUpdatePaketDateBack] = useState();
  const [paketUpdateType, setUpdatePaketType] = useState();
  const [paketUpdateQuantity, setUpdateQuantity] = useState();
  const [paketUpdateReysInfo, setUpdatePaketReysInfo] = useState();
  const [paketUpdateAviaCompany, setUpdatePaketAviaCompany] = useState();
  const [paketUpdateMadinaHotel, setUpdatePaketMadinaHotel] = useState();
  const [paketUpdateMadinaDuration, setUpdatePaketMadinaDuration] = useState();
  const [paketUpdateMadinaDish, setUpdatePaketMadinaDish] = useState();
  const [paketUpdateMakkaHotel, setUpdatePaketMakkaHotel] = useState();
  const [paketUpdateMakkaDuration, setUpdatePaketMakkaDuration] = useState();
  const [paketUpdateMakkaDish, setUpdatePaketMakkaDish] = useState();
  const [paketUpdateDescription, setUpdatePaketDescription] = useState();
  const [paketUpdateDuration, setUpdatePaketDuration] = useState();

  const [paketData, setPaketData] = useState();
  const [filterType, setFilterType] = useState("");
  const [search, setSearch] = useState("");
  const [month, setMonth] = useState("");
  const [modal2, setModal2] = useState("false");
  const [mod, setMod] = useState("false");
  const [currPaket, setCurrPaket] = useState("");

  const addPaket = () => {
    axios
      .post(
        API_PATH + "main/paket-create/",
        {
          name: paketName,
          price: paketPrice,
          date_go: paketDateGo,
          date_back: paketDateBack,
          type_paket: paketType,
          quantity: paketQuantity,
          reys: paketReysInfo,
          avia_company: paketAviaCompany,
          madina_hotel: paketMadinaHotel,
          madina_duration: paketMadinaDuration,
          madina_dish: paketMadinaDish,
          makka_hotel: paketMakkaHotel,
          makka_duration: paketMakkaDuration,
          makka_dish: paketMakkaDish,
          description: paketDescription,
          duration: paketDuration,
        },
        CONFIG
      )
      .then((res) => {
        console.log(res.data);
        setMod(false);
        document.location.reload();
      });
  };

  const getPakets = () => {
    axios
      .get(
        API_PATH +
          `main/paket-list?search=${search}&paket_type=${filterType}&month=${month}`,
        CONFIG
      )
      .then((res) => {
        setPaketData(res.data);
      });
  };

  useEffect(() => {
    getPakets();
  }, [search, month, filterType]);

  const getPaketByID = (id) => {
    axios.get(API_PATH + `main/paket-update/${id}/`, CONFIG).then((res) => {
      console.log(res.data);
      setCurrPaket(id);
      setUpdatePaketName(res.data.name);
      setUpdatePaketPrice(res.data.price);
      setUpdatePaketDateGo(res.data.date_go);
      setUpdatePaketDateBack(res.data.date_back);
      setUpdatePaketType(res.data.type_paket);
      setUpdateQuantity(res.data.quantity);
      setUpdatePaketReysInfo(res.data.reys);
      setUpdatePaketAviaCompany(res.data.avia_company);
      setUpdatePaketMadinaHotel(res.data.madina_hotel);
      setUpdatePaketMadinaDuration(res.data.madina_duration);
      setUpdatePaketMadinaDish(res.data.madina_dish);
      setUpdatePaketMakkaHotel(res.data.makka_hotel);
      setUpdatePaketMakkaDuration(res.data.makka_duration);
      setUpdatePaketMakkaDish(res.data.makka_dish);
      setUpdatePaketDescription(res.data.description);
      setUpdatePaketDuration(res.data.duration);
      setModal2(!modal2);
    });
  };

  const closeModal2 = () => {
    setModal2(!modal2);
    setCurrPaket("");
    setUpdatePaketName("");
    setUpdatePaketPrice("");
    setUpdatePaketDateGo("");
    setUpdatePaketDateBack("");
    setUpdatePaketType("");
    setUpdateQuantity("");
    setUpdatePaketReysInfo("");
    setUpdatePaketAviaCompany("");
    setUpdatePaketMadinaHotel("");
    setUpdatePaketMadinaDuration("");
    setUpdatePaketMadinaDish("");
    setUpdatePaketMakkaHotel("");
    setUpdatePaketMakkaDuration("");
    setUpdatePaketMakkaDish("");
    setUpdatePaketDescription("");
    setUpdatePaketDuration("");
  };

  const updatePaket = () => {
    console.log(paketUpdateQuantity);
    axios
      .patch(
        API_PATH + `main/paket-update/${currPaket}/`,
        {
          name: paketUpdateName,
          price: paketUpdatePrice,
          date_go: paketUpdateDateGo,
          date_back: paketUpdateDateBack,
          type_paket: paketUpdateType,
          quantity: paketUpdateQuantity,
          reys: paketUpdateReysInfo,
          avia_company: paketUpdateAviaCompany,
          madina_hotel: paketUpdateMadinaHotel,
          madina_duration: paketUpdateMadinaDuration,
          madina_dish: paketUpdateMadinaDish,
          makka_hotel: paketUpdateMakkaHotel,
          makka_duration: paketUpdateMakkaDuration,
          makka_dish: paketUpdateMakkaDish,
          description: paketUpdateDescription,
          duration: paketUpdateDuration,
        },
        CONFIG
      )
      .then((res) => {
        setModal2(!modal2);
        setCurrPaket("");
        setUpdatePaketName("");
        setUpdatePaketPrice("");
        setUpdatePaketDateGo("");
        setUpdatePaketDateBack("");
        setUpdatePaketType("");
        setUpdateQuantity("");
        setUpdatePaketReysInfo("");
        setUpdatePaketAviaCompany("");
        setUpdatePaketMadinaHotel("");
        setUpdatePaketMadinaDuration("");
        setUpdatePaketMadinaDish("");
        setUpdatePaketMakkaHotel("");
        setUpdatePaketMakkaDuration("");
        setUpdatePaketMakkaDish("");
        setUpdatePaketDescription("");
        setUpdatePaketDuration("");
        document.location.reload();
      });
  };
  return (
    <>
      <div className="Packet">
        <div className="dash_name_box">
          <div className="dash_name">Abd Abd</div>
          <div className="dash_inp">
            <img src="/img/icon_search.png" alt="" />
            <input
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              type="text"
              placeholder="Qidirish"
            />
          </div>
        </div>
        <div className="pac_filtr_box">
          <select
            defaultValue="Standard"
            onChange={(e) => setFilterType(e.target.value)}
            className="pac_sel"
            name=""
            id=""
          >
            <option value="Standard">Standard</option>
            <option value="Comfort">Comfort</option>
            <option value="VIP">VIP</option>
          </select>
          <select
            defaultValue="Oy"
            onChange={(e) => setMonth(e.target.value)}
            className="pac_sel"
            name=""
            id=""
          >
            <option value="01">Yanvar</option>
            <option value="02">Fevral</option>
            <option value="03">Mart</option>
            <option value="04">Aprel</option>
            <option value="05">May</option>
            <option value="06">Iyun</option>
            <option value="07">Iyul</option>
            <option value="08">Avgust</option>
            <option value="09">Sentabr</option>
            <option value="10">Oktabr</option>
            <option value="11">Noyabr</option>
            <option value="12">Dekabr</option>
          </select>
          {/* <select className="pac_sel" name="" id="">
            <option value="">2024</option>
          </select> */}
          <div onClick={() => setMod(!mod)} className="pac_plus">
            <img src="/img/icon_plus.png" alt="" />
            Paket qo’shish
          </div>
        </div>
        <div className="pac_main">
          {paketData &&
            paketData.map((item, index) => (
              <div key={index} className="pac_main_box">
                <div className="pac_main_text">
                  <div className="d-flex align-items-center gap-2">
                    <img src="/img/icon_cal.png" alt="" />
                    <div className="pac_main_h">{item.date_go}</div>
                  </div>
                  <img
                    onClick={() => getPaketByID(item.id)}
                    style={{ cursor: "pointer" }}
                    src="/img/icon_pen.png"
                    alt=""
                  />
                </div>
                <div className="pac_main_text">
                  <div className="d-flex align-items-center justify-content-between w-100">
                    <div className="pac_main_type">
                      {item.type_paket} - {item.duration} kun
                    </div>
                    <div className="pac_main_p">
                      {item.current_quantity}/{item.quantity}
                    </div>
                  </div>
                </div>
                <Link to={`/paket/${item.id}`} className="pac_main_btn">
                  <div className="pac_btn_h">{item.name} </div>
                  <div className="pac_btn_p">{item.price} $</div>
                </Link>
              </div>
            ))}
        </div>
      </div>

      <div className={`modalcha ${mod ? "active" : ""}`}>
        <div className="d-flex flex-column justify-content-between h-100">
          <form action="" onSubmit={addPaket}>
            <div className="mod_text">
              <div className="mod_name">
                <div className="mod_name_h">Paket qo’shish</div>
                <img
                  onClick={() => setMod(true)}
                  className={``}
                  src="/img/icon_x.png"
                  alt=""
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Tur Paket Nomi </div>
                <input
                  value={paketName}
                  onChange={(e) => setPaketName(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="17-mart Standard Rahmat To'plami"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Uchish kuni va vaqti </div>
                <input
                  value={paketDateGo}
                  onChange={(e) => setPaketDateGo(e.target.value)}
                  className="mod_text_inp"
                  type="date"
                  placeholder="02.28.2024"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Qaytish kuni va vaqti</div>
                <input
                  value={paketDateBack}
                  onChange={(e) => setPaketDateBack(e.target.value)}
                  className="mod_text_inp"
                  type="date"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h"> Safar davomiyligi kun</div>
                <input
                  value={paketDuration}
                  onChange={(e) => setPaketDuration(e.target.value)}
                  className="mod_text_inp"
                  type="number"
                  placeholder="14 kun"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Paket Turi</div>
                <select
                  defaultValue="Standart"
                  onChange={(e) => setPaketType(e.target.value)}
                  className="mod_text_inp"
                  name=""
                  id=""
                >
                  <option value="Standard">Standard</option>
                  <option value="Comfort">Comfort</option>
                  <option value="VIP">VIP</option>
                </select>
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Narxi $</div>
                <input
                  value={paketPrice}
                  onChange={(e) => setPaketPrice(e.target.value)}
                  className="mod_text_inp"
                  type="number"
                  placeholder="$ 1470"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Reys Ma’lumotlari</div>
                <input
                  value={paketReysInfo}
                  onChange={(e) => setPaketReysInfo(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="Toshkent-Jidda-Toshkent"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Avia kompaniya </div>
                <input
                  value={paketAviaCompany}
                  onChange={(e) => setPaketAviaCompany(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="Qanot Sharq"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Paket Joylar soni _ ta </div>
                <input
                  value={paketQuantity}
                  onChange={(e) => setQuantity(e.target.value)}
                  className="mod_text_inp"
                  type="number"
                  placeholder="100"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Madina Hotel</div>
                <input
                  value={paketMadinaHotel}
                  onChange={(e) => setPaketMadinaHotel(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="Al-Ameen  (2-qatorda)"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Madina da davomiyligi</div>
                <input
                  value={paketMadinaDuration}
                  onChange={(e) => setPaketMadinaDuration(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="3-4 kun"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Madinada ovqatlanish </div>
                <input
                  value={paketMadinaDish}
                  onChange={(e) => setPaketMadinaDish(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="2-mahal"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Makka Hotel</div>
                <input
                  value={paketMakkaHotel}
                  onChange={(e) => setPaketMakkaHotel(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="Batoul-Ajiyad  ( 1 km )"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Makka da davomiyligi</div>
                <input
                  value={paketMakkaDuration}
                  onChange={(e) => setPaketMakkaDuration(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="10-11 kun"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Makkada ovqatlanish</div>
                <input
                  value={paketMakkaDish}
                  onChange={(e) => setPaketMakkaDish(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="2-mahal"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Qo'shimcha</div>
                <input
                  value={paketDescription}
                  onChange={(e) => setPaketDescription(e.target.value)}
                  className="mod_text_inp"
                  type="textarea"
                  placeholder="Qo'shimcha izohlar"
                />
              </div>
            </div>
            <div className="mod_btn">
              <button type="submit">
                <img src="/img/icon_plus.png" alt="" />
                Paket qo’shish
              </button>
            </div>
          </form>
        </div>
      </div>

      <div className={`modalcha ${modal2 ? "active" : ""}`}>
        <div className="d-flex flex-column justify-content-between h-100">
          <form onSubmit={updatePaket} action="">
            <div className="mod_text">
              <div className="mod_name">
                <div className="mod_name_h">Paket O'zgartirish</div>
                <img
                  onClick={() => closeModal2()}
                  src="/img/icon_x.png"
                  alt=""
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Tur Paket Nomi </div>
                <input
                  required
                  defaultValue={paketUpdateName}
                  onChange={(e) => setUpdatePaketName(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="17-mart Standard Rahmat To'plami"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Uchish kuni va vaqti </div>
                <input
                  required
                  defaultValue={paketUpdateDateGo}
                  onChange={(e) => setUpdatePaketDateGo(e.target.value)}
                  className="mod_text_inp"
                  type="date"
                  placeholder="02.28.2024"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Qaytish kuni va vaqti</div>
                <input
                  required
                  defaultValue={paketUpdateDateBack}
                  onChange={(e) => setUpdatePaketDateBack(e.target.value)}
                  className="mod_text_inp"
                  type="date"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h"> Safar davomiyligi kun</div>
                <input
                  required
                  defaultValue={paketUpdateDuration}
                  onChange={(e) => setUpdatePaketDuration(e.target.value)}
                  className="mod_text_inp"
                  type="number"
                  placeholder="14 kun"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Paket Turi</div>
                <select
                  defaultValue={paketUpdateType}
                  onChange={(e) => setUpdatePaketType(e.target.value)}
                  className="mod_text_inp"
                  name=""
                  id=""
                >
                  <option value="Standard">Standard</option>
                  <option value="Comfort">Comfort</option>
                  <option value="VIP">VIP</option>
                </select>
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Narxi $</div>
                <input
                  required
                  defaultValue={paketUpdatePrice}
                  onChange={(e) => setUpdatePaketPrice(e.target.value)}
                  className="mod_text_inp"
                  type="number"
                  placeholder="$ 1470"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Reys Ma’lumotlari</div>
                <input
                  required
                  defaultValue={paketUpdateReysInfo}
                  onChange={(e) => setUpdatePaketReysInfo(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="Toshkent-Jidda-Toshkent"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Avia kompaniya </div>
                <input
                  required
                  defaultValue={paketUpdateAviaCompany}
                  onChange={(e) => setUpdatePaketAviaCompany(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="Qanot Sharq"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Paket Joylar soni _ ta </div>
                <input
                  required
                  defaultValue={paketUpdateQuantity}
                  onChange={(e) => setUpdateQuantity(e.target.value)}
                  className="mod_text_inp"
                  type="number"
                  placeholder="100"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Madina Hotel</div>
                <input
                  required
                  defaultValue={paketUpdateMadinaHotel}
                  onChange={(e) => setUpdatePaketMadinaHotel(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="Al-Ameen  (2-qatorda)"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Madina da davomiyligi</div>
                <input
                  required
                  defaultValue={paketUpdateMadinaDuration}
                  onChange={(e) => setUpdatePaketMadinaDuration(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="3-4 kun"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Madinada ovqatlanish </div>
                <input
                  required
                  defaultValue={paketUpdateMadinaDish}
                  onChange={(e) => setUpdatePaketMadinaDish(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="2-mahal"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Makka Hotel</div>
                <input
                  required
                  defaultValue={paketUpdateMakkaHotel}
                  onChange={(e) => setUpdatePaketMakkaHotel(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="Batoul-Ajiyad  ( 1 km )"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Makka da davomiyligi</div>
                <input
                  required
                  defaultValue={paketUpdateMakkaDuration}
                  onChange={(e) => setUpdatePaketMakkaDuration(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="10-11 kun"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Makkada ovqatlanish</div>
                <input
                  required
                  defaultValue={paketUpdateMakkaDish}
                  onChange={(e) => setUpdatePaketMakkaDish(e.target.value)}
                  className="mod_text_inp"
                  type="text"
                  placeholder="2-mahal"
                />
              </div>
              <div className="mod_text_box">
                <div className="mod_text_h">Qo'shimcha</div>
                <input
                  required
                  defaultValue={paketUpdateDescription}
                  onChange={(e) => setUpdatePaketDescription(e.target.value)}
                  className="mod_text_inp"
                  type="textarea"
                  placeholder="Qo'shimcha izohlar"
                />
              </div>
            </div>
            <div className="mod_btn">
              <button type="submit">
                <img src="/img/icon_plus.png" alt="" />
                Paket o'zgartirish
              </button>
            </div>
          </form>
        </div>
      </div>
    </>
  );
};

export default Packet;
