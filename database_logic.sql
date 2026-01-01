-- 1. Creación de la vista principal para reportes
-- Esta vista consolida la información de ventas, productos y sucursales
CREATE OR REPLACE VIEW vista_reporte_general AS
SELECT 
    v.fecha,
    v.cantidad,
    p.nombre AS producto,
    p.precio,
    s.ciudad,
    s.region,
    (v.cantidad * p.precio) AS total_venta 
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
JOIN sucursales s ON v.id_sucursal = s.id_sucursal;
/*SELECT * FROM vista_reporte_general*/
-- 2. Consulta de recaudación por región
-- Útil para identificar el rendimiento geográfico de las ventas
SELECT 
    region, 
    SUM(total_venta) AS recaudacion_total
FROM vista_reporte_general
GROUP BY region
ORDER BY recaudacion_total DESC;

-- 3. Análisis de Ticket Promedio por Ciudad
SELECT 
    ciudad,
    ROUND(AVG(total_venta)::numeric, 2) AS ticket_promedio,
    COUNT(*) AS cantidad_operaciones
FROM vista_reporte_general
GROUP BY ciudad
ORDER BY ticket_promedio DESC;