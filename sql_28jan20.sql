use toko;

select * from toko where (kotaId = 1 or 
kotaId = 3) and (totalIncome between 5000 and 7000)
and tanggalBerdiri in (2015,2017)
 order by totalIncome desc;
 
select count(*) as count_kota_2, min(totalIncome),
 max(totalIncome), sum(totalIncome), avg(totalIncome)
 from toko where tanggalBerdiri in (2015,2017)
 group by kotaId having count_kota_2 < 10
 order by count_kota_2; 
 
 truncate pelanggan;
 
 select t.nama as nama_toko, k.nama as nama_kota, totalIncome 
 from toko t join kota k on t.kotaId = k.id;

insert into pelanggan 
values(null, 'Joko', 4, 3), 
(null, 'Sari', 3, 1), (null, 'Kuda', 1, 13);

 
select k.nama as nama_kota, sum(totalIncome) as Total_pendapatan
from toko t join kota k on t.kotaId = k.id 
group by nama_kota having Total_pendapatan >70000;



select p.nama, nama_kota_toko, nama_toko from
(select k.nama as nama_kota_toko, t.nama as nama_toko, 
tanggalBerdiri, t.id as tokoId
from toko t join kota k on t.kotaId = k.id) k_t 
join pelanggan p on p.tokoId = k_t.tokoId;



select nama_pelanggan, k.nama as nama_kota_pelanggan, 
totalIncome, tanggalBerdiri from 
(select p.nama as nama_pelanggan, p.kotaId, totalIncome, 
tanggalBerdiri from 
pelanggan p join toko t on p.tokoId = t.id) p_t join 
kota k on p_t.kotaId = k.id having tanggalBerdiri in (2017);

create view contoh as select p.nama as nama_pelanggan, p.kotaId, 
totalIncome, 
tanggalBerdiri from 
pelanggan p join toko t on p.tokoId = t.id;

select * from contoh;

select nama, totalIncome, if(totalIncome < 5000, "Less than 5000",
 "More than 5000") as explanatory
from toko;


select *, 
(case 
	when totalIncome < 5000 then 'Less than 5000'
    when totalIncome between 5000 and 7000 then '5000-7000'
    else 'more than 7000'
end) as explanatory
from toko;



